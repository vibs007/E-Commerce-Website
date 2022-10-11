from email.policy import default
from statistics import mode
from django.db import models
from matplotlib.image import thumbnail

# Create your models here.
class BlogPost(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)
    head0 = models.CharField(max_length = 100)
    chead0 = models.CharField(max_length = 10000)
    head1 = models.CharField(max_length = 100)
    chead1 = models.CharField(max_length = 10000)
    head2 = models.CharField(max_length = 100)
    chead2 = models.CharField(max_length = 10000)
    pub_date = models.DateField()
    publisher = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title