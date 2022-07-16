from django.shortcuts import get_object_or_404, render #404 is a shortcut to get info from db and if it doesnot it returns error
from .models import Category, Product

#functions

def product_all(request):
    products = Product.objects.all() #running a Sql quary on the table in db collecting data into this variable
    return render(request, 'store/home.html', {'products': products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/products/single.html', {'product': product})

