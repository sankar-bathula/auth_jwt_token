from rest_framework.serializers import ModelSerializer
from auth_jwt_token_app.models import Products

class ProductsSerializers(ModelSerializer):
	class Meta:
		model = Products
		fields = "__all__"