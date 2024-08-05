from django.db import models
import uuid;
from django.utils.text import slugify 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime,date
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


#for unique value generation

# Create your models here.









# handling product info 

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    
class Orders(models.Model):
    Customer_name = models.CharField(max_length=100,default="demo")
    productid = models.IntegerField(default=None)
    product_name = models.CharField(max_length=100,default="demo")
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    
    
class SalesReports(models.Model):
    totalSale = models.IntegerField(default=0)
    totalProfit = models.IntegerField(default=0)
    totalQuantity = models.IntegerField(default=0)
    date_From = models.DateField(default=date(2021, 6, 15))
    date_to = models.DateField(default= date(2021, 6, 15))

    




    # form data handling

class ContactForm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    #Biling Form

class BilingForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    code = models.IntegerField()



    






    