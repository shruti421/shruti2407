from django.db import models

class Product(models.Model):

    product_id =  models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image_link = models.CharField(max_length=250,default='')
    image_link2 = models.CharField(max_length=250,default='')
    # image = models.ImageField(upload_to='shopo/images',default='')

    def __str__(self):
        return self.product_name
    
