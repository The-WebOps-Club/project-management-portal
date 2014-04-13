
from django import template
from django.shortcuts import get_object_or_404
from userprofile.models import *
register = template.Library()

@register.assignment_tag
def profile(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return get_object_or_404( UserProfile, user=qs)