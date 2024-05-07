from django.shortcuts import render
from . import models

def index(request):
    products = models.Product.objects.all()
    category = models.Category.objects.all()
    context = {
        'products':products,
        'category':category,
    }


    return render(request, 'index.html', context)