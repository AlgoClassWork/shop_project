from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category
# Create your views here.
# http://127.0.0.1:8000/
def product_list(request, slug=None):
    products = Product.objects.filter(available=True)
    # http://127.0.0.1:8000/category/elektronika
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)

    context = {'products': products, 'categories': categories}
    return render(request, 'product_list.html', context)

# http://127.0.0.1:8000/product/mylo
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

# http://127.0.0.1:8000/cart/
def cart_detail(request):
    cart = request.session.get('cart', {})
    product_slugs = cart.keys() 
    products = Product.objects.filter(slug__in=product_slugs)
    cart_products = []
    total_price = 0

    for product in products:
        quantity = cart[product.slug]
        total_item = product.price * quantity
        cart_products.append( {'product': product, 'quantity': quantity, 'total_price': total_item} )
        total_price += total_item

    context = {'cart_products': cart_products, 'total_price': total_price}
    return render(request, 'cart_detail.html', context)

# http://127.0.0.1:8000/cart/add/zaporochez
def cart_add(request, slug):
    cart = request.session.get('cart', {})
    quantity = cart.get( slug, 0 ) + 1
    cart[slug] = quantity
    request.session['cart'] = cart
    return redirect( 'product_list' )

# http://127.0.0.1:8000/cart/remove/noutbuk
def cart_remove(request, slug):
    return redirect('cart_detail')
