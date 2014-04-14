# permissions.py
# utlity classes for handling permissions.

# permission model contains static methods to compute permissions for a given user for a particular task.
# still incomplete. abstract idea. may be dropped.

from project.models import *
class PermissionHandler:
	@staticmethod
	def create_update( user, **kwargs ):
		return 1
		p_id = kwargs['project']
		
		p = Project.objects.filter( pk = p_id )[0]
		if( user in p.users.all() or user in p.mentors.all()):
			return 1
		else:
			return 0


	@staticmethod
	def view_update( user, **kwargs ):
		if user.is_authenticated():
			return 1
		else:
			return 0
	@staticmethod
	def create_task( user, **kwargs ):
		return 1

	@staticmethod
	def create_club( user, **kwargs ):
		return 1

	@staticmethod
	def create_project( user, **kwargs ):
		return 1

	@staticmethod
	def create_comment( user, **kwargs ):
		return 1

	@staticmethod
	def edit_club( user, **kwargs ):
		return 1

	@staticmethod
	def add_core_to_club( user, **kwargs ):
		return 1

	@staticmethod
	def edit_project( user, **kwargs ):
		return 1
		p_id = kwargs['project']
		
		p = Project.objects.filter( pk = p_id )[0]
		if( user in p.mentors.all()):
			return 1
		else:
			return 0
	@staticmethod
	def delete_document( user, **kwargs ):
		return 1