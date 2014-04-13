from django.shortcuts import render
from userprofile.forms import *
from userprofile.models import *
from django.contrib.auth.decorators import login_required

@login_required
def account(request):
	cd1 = {'user': request.user}
	return render(request, 'user/edit_account.html', cd1)

def test(request):
	return render(request, 'registration/base.html', {'user': request.user})	
