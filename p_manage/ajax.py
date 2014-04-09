from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from userprofile.models import UserProfile
from django.template.loader import render_to_string
from django.template.context import RequestContext
from dajaxice.utils import deserialize_form

@dajaxice_register
def get_account(request):
	dajax = Dajax()
	user1 = UserProfile.objects.get(user.username=request.user.username)
	cd1 = {'user' : user1}
	html1 = render_to_string('user/edit_account.html', cd1, RequestContext(request))
	dajax.assign('#var_content', 'innerHTML', html1)
