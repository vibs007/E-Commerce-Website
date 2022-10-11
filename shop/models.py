from email.policy import default
from operator import mod
from statistics import mode
from unittest.util import _MAX_LENGTH
from xml.etree.ElementTree import tostring
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to ='shop/images', default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msgt_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=1000, default="")
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length = 20000)
    name = models.CharField(max_length = 20000)
    email = models.CharField(max_length = 20000)
    address = models.CharField(max_length = 20000)
    city = models.CharField(max_length = 20000)
    state = models.CharField(max_length = 20000)
    zip_code = models.CharField(max_length = 20000)
    phone = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.order_id}"

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=10000)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)


    def __str__(self):
        return self.update_desc[0:10]+".."

