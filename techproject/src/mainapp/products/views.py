from django.http import HttpResponse
from django.shortcuts import render
from . import models
from models import Product


def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})


# Create your views here.
