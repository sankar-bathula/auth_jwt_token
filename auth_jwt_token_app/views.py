from django.shortcuts import render
from auth_jwt_token_app.models import Products
from auth_jwt_token_app.serializers import ProductsSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.views.decoraters.csrf import csrf_exempt
# from django.utils.decorators import method_decorators
# @method_decorator(csrf_exempt, name='dispatch')
class ProductsAPI(ModelViewSet):
	serializer_class = ProductsSerializers
	queryset = Products.objects.all()

	authentication_classes =[JSONWebTokenAuthentication,]
	#authentication_classes =[BasicAuthentication,]
	permissions_classes = [IsAuthenticated,] 