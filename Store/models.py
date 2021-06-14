from django.db import models


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    displayName = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=419)
    coverImage = models.ImageField(upload_to="product/images", null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images/')

    def __str__(self):
        return self.product.name
