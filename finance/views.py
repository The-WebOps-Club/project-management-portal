from django.shortcuts import render
from finance.models import *
from finance.forms import *
from project.models import Project
from userprofile.models import UserProfile
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import HiddenInput


def core_home(request):
	pass

def core_advance(request):
	user = UserProfile.objects.get(user=request.user)
	if not user.is_finance_core:
		raise Http404

	form_fail_p = False
	form_fail_a = False
	form_fail_i = False
	if request.method == 'POST':
		if request.POST['form_type'] == 'pending':
			formset = CoreApprovalFormset(request.POST)
			if formset.is_valid():
				formset.save()
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
	cd.update({'form_fail_i': form_fail_i, 'form_fail_p': form_fail_p, 'form_fail_a': form_fail_a})
	return render(request, 'finance/core_advance.html', cd)

def core_reimb(request):
	pass

def project_info(request, project_id):
	pass

def project_advance(request, project_id):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	if not user.is_in(project):
		raise Http404	
	advances = Advance.objects.filter(project=project).order_by('applied_date')
	new_adv_form = NewAdvanceForm(initial={'project':project,})
	cd = {'user': request.user, 'project': project, 'new_form': new_adv_form, 'advances': advances}

	if request.method == 'POST':
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
		cd.update({'extra_form': extra_form, 'is_mentor': True, 'new_req_forms': mentor_forms})
		cd['formset_data'] = formset.management_form

	return render(request, 'finance/project_advance.html', cd)

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
	reimbs = Reimbursement.objects.filter(project=project).order_by('applied_date')
	bill_form = BillForm()
	bill_fail = False
	no_bills = True
	if request.method == 'POST':
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
	if initial and col_id:
		return HttpResponseRedirect(reverse('finance:project_reimbursement_2', args=[project.id, col_id]))
	return render(request, 'finance/project_reimbursement.html', cd)

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
	bill_form = BillForm()
	bill_fail = False
	no_bills = ob.bills.all().count()==0

	if request.method == 'POST':
		b = BillForm(request.POST, request.FILES)
		if b.is_valid():
			bi = b.save()
			bill_form = BillForm()
			ob.bills.add(bi)
		else:
			bill_form = b
			bill_fail = True

	cd = {'user': request.user, 'project': project, 'objects': objects, 'ob': ob, 'no_bills': no_bills, 'bill_form': bill_form,}
	cd['bill_fail'] = bill_fail
	return render(request, 'finance/bills.html', cd)
