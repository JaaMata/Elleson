from django.db import models
from Store.models import *
# Create your models here.
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)