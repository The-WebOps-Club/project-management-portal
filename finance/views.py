from django.shortcuts import render
from finance.models import *
from finance.forms import *
from project.models import Project
from userprofile.models import UserProfile
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.forms import HiddenInput
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def core_home(request):
	user = UserProfile.objects.get(user=request.user)
	if not user.is_finance_core:
		raise Http404
	b_infos = BudgetInfo.objects.all()
	years = Project.objects.all().values('year').distinct()
	a = []
	for y in years:
		a.append(y['year'])
	a.sort(reverse=True)
	cd = {'user': request.user, 'projects': b_infos, 'years': a, 'least': a[0],}
	return render(request, 'finance/core_home.html', cd)

@login_required
def core_advance(request):
	user = UserProfile.objects.get(user=request.user)
	if not user.is_finance_core:
		raise Http404

	post = False
	form_fail_p = False
	form_fail_a = False
	form_fail_i = False
	if request.method == 'POST':
		post = True
		if request.POST['form_type'] == 'pending':
			formset = CoreApprovalFormset(request.POST)
			if formset.is_valid():
				new = formset.save()
				for n in new:
					if n.is_app_core == 'approved':
						n.approved_date = date.today()
						n.save()
			else:
				form_fail_p = True
				pending_forms = formset
		elif request.POST['form_type'] == 'new_ins':
			new = InstallmentForm(request.POST)
			if new.is_valid():
				adv = Advance.objects.get(id=request.POST['adv_id'])
				n = new.save()
				adv.installments.add(n)
			else:
				form_fail_i = True
				install_form = new
		else:
			formset = CoreApprovedFormset(request.POST)
			if formset.is_valid():
				formset.save()
			else:
				form_fail_a = True
				approved_forms = formset

	pending = Advance.objects.filter(is_app_core='pending').filter(is_app_mentor='approved').order_by('-applied_date')
	approved = Advance.objects.filter(is_app_core='approved').order_by('applied_date')
	if not form_fail_p:
		pending_forms = CoreApprovalFormset(queryset=pending)
	if not form_fail_a:
		approved_forms = CoreApprovedFormset(queryset=approved)
	if not form_fail_i:
		install_form = InstallmentForm()
	pen = []
	app = []
	for p in range(len(pending)):
		pen.append([pending[p], pending_forms[p]])
	for p in range(len(approved)):
		app.append([approved[p], approved_forms[p]])	
	cd = {'user': request.user, 'pending': pen, 'approved': app, 'p_extra': pending_forms[-1], 'a_extra': approved_forms[-1]}
	cd['p_data'] = pending_forms.management_form
	cd['a_data'] = approved_forms.management_form
	cd['new_ins_form'] = install_form
	cd.update({'form_fail_i': form_fail_i, 'form_fail_p': form_fail_p, 'form_fail_a': form_fail_a, 'post': post})
	return render(request, 'finance/core_advance.html', cd)

@login_required
def core_reimb(request):
	user = UserProfile.objects.get(user=request.user)
	if not user.is_finance_core:
		raise Http404

	post = False
	form_fail_p = False
	form_fail_a = False
	form_fail_i = False
	if request.method == 'POST':
		post = True
		if request.POST['form_type'] == 'pending':
			formset = CoreApprovalFormset2(request.POST)
			if formset.is_valid():
				new = formset.save()
				print new
				for n in new:
					if n.is_app_core == 'approved':
						n.approved_date = date.today()
						n.save()
			else:
				form_fail_p = True
				pending_forms = formset
		elif request.POST['form_type'] == 'new_ins':
			new = InstallmentForm(request.POST)
			if new.is_valid():
				adv = Reimbursement.objects.get(id=request.POST['adv_id'])
				n = new.save()
				adv.installments.add(n)
			else:
				form_fail_i = True
				install_form = new
		else:
			formset = CoreApprovedFormset2(request.POST)
			if formset.is_valid():
				formset.save()
			else:
				form_fail_a = True
				approved_forms = formset

	pending = Reimbursement.objects.filter(is_app_core='pending').filter(is_app_mentor='approved').order_by('-applied_date')
	approved = Reimbursement.objects.filter(is_app_core='approved').order_by('applied_date')
	if not form_fail_p:
		pending_forms = CoreApprovalFormset2(queryset=pending)
	if not form_fail_a:
		approved_forms = CoreApprovedFormset2(queryset=approved)
	if not form_fail_i:
		install_form = InstallmentForm()
	pen = []
	app = []
	for p in range(len(pending)):
		pen.append([pending[p], pending_forms[p]])
	for p in range(len(approved)):
		app.append([approved[p], approved_forms[p]])	
	cd = {'user': request.user, 'pending': pen, 'approved': app, 'p_extra': pending_forms[-1], 'a_extra': approved_forms[-1]}
	cd['p_data'] = pending_forms.management_form
	cd['a_data'] = approved_forms.management_form
	cd['new_ins_form'] = install_form
	cd.update({'form_fail_i': form_fail_i, 'form_fail_p': form_fail_p, 'form_fail_a': form_fail_a, 'post': post})
	return render(request, 'finance/core_reimbursement.html', cd)

@login_required
def project_info(request, project_id):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	if not user.is_in(project) and not user.is_finance_core:
		raise Http404	
	advances = Advance.objects.filter(project=project)
	reimbs = Reimbursement.objects.filter(project=project)
	info = BudgetInfo.objects.get(project=project)
	cd = {'advances': advances, 'reimbs': reimbs, 'info':info, 'project': project, 'user': request.user,}
	return render(request, 'finance/project_info.html', cd)

@login_required
def project_advance(request, project_id):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	if not user.is_in(project):
		raise Http404	
	post = False
	advances = Advance.objects.filter(project=project).order_by('applied_date')
	new_adv_form = NewAdvanceForm(initial={'project':project,})
	cd = {'user': request.user, 'project': project, 'new_form': new_adv_form, 'advances': advances}

	if request.method == 'POST':
		post = True
		if request.POST['form_type'] == 'new_advance':
			new_adv = NewAdvanceForm(request.POST)
			if new_adv.is_valid():
				new_adv.save()
			else:
				cd['new_form'] = new_adv
		else:
			formset = MentorApprovalFormset(request.POST, prefix='mentor_formset')
			if formset.is_valid():
				formset.save()

	if user.is_mentor(project):
		mentor_forms = []
		queryset=Advance.objects.filter(is_app_mentor='pending').order_by('applied_date')
		formset = MentorApprovalFormset(queryset=queryset, prefix='mentor_formset')
		for i in range(len(queryset)):
			mentor_forms.append([queryset[i], formset[i]])
		extra_form = formset[-1]
		cd.update({'extra_form': extra_form, 'is_mentor': True, 'new_req_forms': mentor_forms, 'post': post})
		cd['formset_data'] = formset.management_form

	return render(request, 'finance/project_advance.html', cd)

@login_required
def project_reimb(request, project_id, col_id=None):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	cd={}
	if not user.is_in(project):
		raise Http404
	if not col_id:
		initial = True
	else:
		initial = False
	post = False
	reimbs = Reimbursement.objects.filter(project=project).order_by('applied_date')
	bill_form = BillForm()
	bill_fail = False
	no_bills = True
	if request.method == 'POST':
		post = True
		if request.POST['form_type'] == 'add_bill':
			b = BillForm(request.POST, request.FILES)
			if b.is_valid():
				bi = b.save()
				bill_form = BillForm()
				if initial:
					col = Collection()
					col.save()
					col_id = col.id
				else:
					col = Collection.objects.get(id=col_id)
				col.bills.add(bi)
			else:
				bill_form = b
				bill_fail = True
		else:
			formset = MentorApprovalFormset2(request.POST, prefix='mentor_formset')
			if formset.is_valid():
				new = formset.save()

	if user.is_mentor(project):
		mentor_forms = []
		queryset=Reimbursement.objects.filter(is_app_mentor='pending').order_by('applied_date')
		formset = MentorApprovalFormset2(queryset=queryset, prefix='mentor_formset')
		for i in range(len(queryset)):
			mentor_forms.append([queryset[i], formset[i]])
		extra_form = formset[-1]
		cd.update({'extra_form': extra_form, 'is_mentor': True, 'new_req_forms': mentor_forms})
		cd['formset_data'] = formset.management_form

	if col_id:
		col = Collection.objects.get(id=col_id)
		cd['col'] = col
		no_bills = col.bills.all().count() == 0
	cd.update({'user': request.user, 'project': project, 'reimbs': reimbs, 'bill_fail': bill_fail, 'no_bills': no_bills, 'bill_form': bill_form,})
	cd['post'] = post
	if initial and col_id:
		return HttpResponseRedirect(reverse('finance:project_reimbursement_2', args=[project.id, col_id]))
	return render(request, 'finance/project_reimbursement.html', cd)

@login_required
def project_reimb_save(request, project_id, col_id):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	if not user.is_in(project):
		raise Http404
	col = Collection.objects.get(id=col_id)
	r = Reimbursement(project=project)
	r.save()
	for c in col.bills.all():
		r.bills.add(c)
	col.delete()
	return HttpResponseRedirect(reverse('finance:project_reimbursement', args=[project.id]))

@login_required
def project_bills(request, project_id, objects, object_id):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	if user.is_in(project):
		is_in = True
	elif user.is_finance_core:
		is_in = False
	else:
		raise Http404
	if objects == 'advance':
		ob = Advance.objects.get(id=object_id)
		if ob.is_app_core != 'approved':
			raise Http404
	elif objects == 'reimbursement':
		ob = Reimbursement.objects.get(id=object_id)
	else:
		raise Http404
	post = False
	bill_form = BillForm()
	bill_fail = False
	no_bills = ob.bills.all().count()==0

	if request.method == 'POST':
		post = True
		b = BillForm(request.POST, request.FILES)
		if b.is_valid():
			bi = b.save()
			bill_form = BillForm()
			ob.bills.add(bi)
		else:
			bill_form = b
			bill_fail = True

	cd = {'user': request.user, 'project': project,'is_in': is_in, 'objects': objects, 'ob': ob, 'no_bills': no_bills, 'bill_form': bill_form,}
	cd['bill_fail'] = bill_fail
	cd['post'] = post
	return render(request, 'finance/bills.html', cd)

def delete_bill(request, objects, object_id):
	if objects == 'bill':
		b = Bill.objects.get(id=object_id)
		b.delete()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	elif objects == 'col':
		c = Collection.objects.get(id=object_id)
		c.delete()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER')[:-2])
	else:
		raise Http404
	