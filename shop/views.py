from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category
# Create your views here.
#http://127.0.0.1:8000/
def product_list(request, slug=None):
    products = Product.objects.filter(available=True)
    #http://127.0.0.1:8000/category/elektronika
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)

    context = {'products': products, 'categories': categories}
    return render(request, 'product_list.html', context)

#http://127.0.0.1:8000/product/mylo
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

#http://127.0.0.1:8000/cart/add/zaporochez
def cart_add(request, slug):
    cart = request.session.get('cart', {})
    product_slug = slug
    quantity = cart.get( product_slug, 0 ) + 1
    cart[product_slug] = quantity
    request.session['cart'] = cart
    print( request.session['cart'] )
    return redirect( 'product_list' )
