from django.shortcuts import render
from finance.models import *
from finance.forms import *
from project.models import Project
from userprofile.models import UserProfile
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse


def core_home(request):
	pass

def core_advance(request):
	pass

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
	if user.is_mentor(project):
		pen_adv = Advance.objects.filter(is_app_mentor=False)
		mentor_forms = []
		for adv in pen_adv:
			mentor_forms.append(MentorApprovalForm(instance=adv))
		cd['new_req_forms'] = mentor_forms

	if request.method == 'POST':
		new_adv = NewAdvanceForm(request.POST)
		if new_adv.is_valid():
			new_adv.save()
		else:
			cd['new_form'] = new_adv
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
		b = BillForm(request.POST, request.FILES)
		if b.is_valid():
			bi = b.save()
			bill_form = BillForm()
			if initial:
				col = Collection()
				col.save()
				col_id = col.id
				print col
			else:
				col = Collection.objects.get(id=col_id)
			col.bills.add(bi)
		else:
			bill_form = b
			bill_fail = True
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
	if not user.is_in(project):
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
