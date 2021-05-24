from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    context = {}
    return render(request, "index.html", context)


def product(request):

    products = Product.objects.all()

    context = {"products": products}
    return render(request, 'product.html', context)
