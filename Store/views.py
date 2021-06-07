from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    context = {}
    return render(request, "index.html", context)


def products(request):

    products = Product.objects.all()

    context = {"products": products}
    return render(request, 'products.html', context)

def product(request, id):

    products = Product.objects.all()
    product = products.get(id=id)

    context = {"product": product}
    return render(request, 'product.html', context)
