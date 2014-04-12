from django.shortcuts import render
from userprofile.forms import *
from userprofile.models import *

def account(request):
	user1 = UserProfile.objects.get(user__id = request.user.id)
	cd1 = {'user': request.user}
	return render(request, 'user/edit_account.html', cd1)

def test(request):
	return render(request, 'user/edit_account1.html', {'user': request.user})	
