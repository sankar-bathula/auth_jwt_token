from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
class CustomeAuthentication(BaseAuthentication):
	def authenticate(self, request):
		username = request.GET.get('username')
		if username is None:
			return None
		try:
			user = User.objects.get(username=username)
		except UserDoesNotExit:
			raise AuthenticationFailed("user not avilable")
		return (user, None)