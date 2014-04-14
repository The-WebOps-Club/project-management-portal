from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from userprofile.models import UserProfile
from userprofile.forms import UserProfileForm
from django.template.loader import render_to_string
from django.template.context import RequestContext
from dajaxice.utils import deserialize_form

@dajaxice_register
def get_profile(request, form1 = None):
	dajax = Dajax()
	if form1 is None:
		try:
			user1 = UserProfile.objects.get(user = request.user)
			form1 = UserProfileForm(instance = user1, initial = {'first_name': user1.user.first_name, 'last_name': user1.user.last_name})
		except:
			form1 = UserProfileForm(initial = {'first_name': request.user.first_name, 'last_name': request.user.last_name})
	cd1 = {'form': form1, 'user': request.user}
	html1 = render_to_string('user/get_form.html', cd1, RequestContext(request))
	dajax.assign('#UpdateDiv', 'innerHTML', html1)
	return dajax.json()

@dajaxice_register
def save_profile(request, form2, img):
	dajax = Dajax()
	try:
		user2 = UserProfile.objects.get(user = request.user)
	except:
		user2 = UserProfile()
	res = UserProfileForm(deserialize_form(form2), instance = user2)
	if not res.is_valid() or res is None:
		cd2 = {'form': res, 'user': request.user}
		html1 = render_to_string('user/get_form.html', cd2, RequestContext(request))
		dajax.assign('#UpdateDiv', 'innerHTML', html1)
		return dajax.json()
	res.save()
	u = request.user
	u.first_name = res.cleaned_data['first_name']
	u.last_name = res.cleaned_data['last_name']
	u.save()
	return get_profile(request)

