# permissions.py
# utlity classes for handling permissions.

# permission model contains static methods to compute permissions for a given user for a particular task.
# still incomplete. abstract idea. may be dropped.
class PermissionModel:

	def create_update( user, **kwargs ):
		p_id = kwargs['project']
		
		p = Project.objects.filter( pk = p_id )[0]
		if( user in p.users + p.mentors):
			return 1
		else:
			return 0

	def view_update( user, **kwargs ):
		if user.is_authenticated():
			return 1
		else:
			return 0

	def create_task( user, **kwargs ):
		pass