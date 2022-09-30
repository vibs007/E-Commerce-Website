from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
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
