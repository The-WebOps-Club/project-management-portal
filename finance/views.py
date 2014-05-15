from django.shortcuts import render
from finance.models import *
from finance.forms import *
from project.models import Project
from userprofile.models import UserProfile
from django.http import Http404


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
	new_adv_form = NewAdvanceForm(initial={'project':project})
	cd = {'user': request.user, 'project': project, 'new_form': new_adv_form, 'advances': advances}
	if user.is_mentor(project):
		pen_adv = Advance.objects.filter(is_app_mentor=False)
		mentor_forms = []
		for adv in pen_adv:
			mentor_forms.append(MentorApprovalForm(instance=adv))
		cd['new_req_forms'] = mentor_forms
	return render(request, 'finance/project_advance.html', cd)

def project_reimb(request, project_id):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	if not user.is_in(project):
		raise Http404
	reimbs = Reimbursement.objects.filter(project=project).order_by('applied_date')

def project_bills(request, project_id, objects, object_id):
	user = UserProfile.objects.get(user=request.user)
	project = Project.objects.get(id=project_id)
	print objects
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
