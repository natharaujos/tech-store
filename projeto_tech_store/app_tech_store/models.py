from django.db import models

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    category = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    productqtt = models.IntegerField()
   
