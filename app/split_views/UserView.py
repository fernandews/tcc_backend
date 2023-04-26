from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse
from http import HTTPStatus

class UserView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


