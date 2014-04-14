from django.shortcuts import render
from userprofile.forms import *
from userprofile.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from userprofile.ajax import get_profile
from dajaxice.utils import deserialize_form

@login_required
def account(request):
	cd1 = {'user': request.user, 'decide': 0, 'form': 0, }
	return render(request, 'user/edit_account.html', cd1)

def test(request):
	return render(request, 'registration/base.html', {'user': request.user})	

def upload(request):
	if request.method == 'POST':
		try:
			user1 = UserProfile.objects.get(user = request.user)
		except:
			user1 = UserProfile(user = request.user)
		form2 = UserProfileForm(request.POST, request.FILES, instance = user1)
		if not form2.is_valid() or form2 is None:
			cd2 = {'user': request.user, 'form': form2, 'decide': 1,}
			return render(request, 'user/edit_account.html', cd2)
		else:
			form2.save()
			u = request.user
			u.first_name = form2.cleaned_data['first_name']
			u.last_name = form2.cleaned_data['last_name']
			u.save()
			return HttpResponseRedirect('/account/user/')