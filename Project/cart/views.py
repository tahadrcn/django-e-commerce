from django.shortcuts import render, redirect, get_object_or_404
from prj.models import product
from cart.cart import Cart


def index(request):
    username = request.session.get('username')  # session'daki değeri alır (get)
    products = product.objects.all()
    context = {
        'username': username,
        'products': products,
    }
    return render(request, 'homepage.html', context=context)

def cart_add(request, id):
    cart = Cart(request)
    product_ = get_object_or_404(product, id=id)
    cart.add(product=product_,
             quantity=1,
             override_quantity=False)
    return redirect('kahveler')

def cart_add_sepet(request, id):
    cart = Cart(request)
    product_ = get_object_or_404(product, id=id)
    cart.add(product=product_,
             quantity=1,
             override_quantity=False)
    return redirect('cart_detail')



def cart_remove(request, id):
    cart = Cart(request)
    product_ = get_object_or_404(product, id=id)
    cart.remove(product_)
    return redirect('cart_detail')

def cart_remove_sepet(request, id):
    cart = Cart(request)
    product_ = get_object_or_404(product, id=id)
    cart.remove_single(product_)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'sepet.html', context=context)
