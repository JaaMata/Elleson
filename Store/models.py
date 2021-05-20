from django.db import models
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name


class Tag(modes.Model):
    name = models.CharField(max_length=200, null=True)

class Product(model.Model):
    name = models.CharField(max_length=200, null=True)
