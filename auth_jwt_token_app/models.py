from django.db import models

# Create your models here.
class Products(models.Model):
	product_id = models.IntegerField()
	product_name = models.CharField(max_length=100)
	product_price = models.FloatField()
	product_location = models.CharField(max_length=100)
	