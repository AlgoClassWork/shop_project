from django.shortcuts import render

from .models import Product
# Create your views here.
#http://127.0.0.1:8000/
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
