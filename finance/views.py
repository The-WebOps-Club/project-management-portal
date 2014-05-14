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

def project_bills(request, project_id):
	pass