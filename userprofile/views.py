from django.shortcuts import render
from userprofile.forms import *
from userprofile.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from userprofile.ajax import get_profile

@login_required
def account(request):
	try:
		user1 = UserProfile.objects.get(user = request.user)
		form1 = UserProfileForm(instance = user1, initial = {'first_name': user1.user.first_name, 'last_name': user1.user.last_name})
	except:
		form1 = UserProfileForm(initial = {'first_name': request.user.first_name, 'last_name': request.user.last_name})
	cd1 = {'form': form1, 'user': request.user}
	return render(request, 'user/edit_account.html', cd1)

def test(request):
	return render(request, 'registration/base.html', {'user': request.user})	

@login_required
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