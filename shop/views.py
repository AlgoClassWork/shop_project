from django.shortcuts import render

from .models import Product
# Create your views here.
#http://127.0.0.1:8000/
def product_list(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'product_list.html', context)
