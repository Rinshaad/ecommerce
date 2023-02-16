from django.db import models
from common.models import Seller

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=20)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    stock = models.IntegerField()
    image = models.ImageField(upload_to = 'products/')
    price = models.FloatField()
    code = models.CharField(max_length=10, default='')


    class Meta:
        db_table = 'product' 