from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField(default=0)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=10,default='')
    status = models.CharField(max_length=10,default='active')

    class Meta:
        db_table = 'customer' 

class Seller(models.Model):
    seller_name =models.CharField(max_length=20)
    email = models.CharField(max_length = 50,default='')
    address = models.CharField(max_length = 200)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length = 15)
    username = models.IntegerField(null=True)
    password = models.CharField(max_length=20,default='')
    company_name = models.CharField(max_length = 30)
    holder_name =  models.CharField(max_length = 20)
    ifsc = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    account_number = models.BigIntegerField()
    image = models.ImageField(upload_to = 'seller/',default='static/image/dummy.jpg' )
    status = models.CharField(max_length = 20, default = 'pending')

    class Meta:
        db_table = 'seller'

    