from django.shortcuts import render

from .models import Product, Category
# Create your views here.
#http://127.0.0.1:8000/
def product_list(request):
    products = Product.objects.filter(available=True)
    #http://127.0.0.1:8000/category/elektronika
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'product_list.html', context)
