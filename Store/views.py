from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    context = {}
    return render(request, "index.html", context)


def product(request):
    products = Product.objects.all()
    images = products.Image.all()

    context = {"products": products, "images": images}
    return render(request, 'product.html', context)
