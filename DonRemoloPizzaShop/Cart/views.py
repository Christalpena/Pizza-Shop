from django.http import HttpResponse
from django.shortcuts import render,redirect
from BeveragesApp.models import Beverage
from PizzaApp.models import Pizza
from .cart import Cart
# Create your views here.


def add_product(request, product_name):
    cart = Cart(request)
    
    try:
        product = Pizza.objects.get(name=product_name)
    except Pizza.DoesNotExist:
        try:
            product = Beverage.objects.get(name=product_name)
        except Beverage.DoesNotExist:
            return HttpResponse("Este producto no existe.")
        else:
            cart.add(product)
            return redirect('beverages')
    else:
        cart.add(product)
        return redirect('pizzas')

def delete_product(request,product_name):
    cart = Cart(request)
    
    try:
        product = Pizza.objects.get(name=product_name)
    except Pizza.DoesNotExist:
        try:
            product = Beverage.objects.get(name=product_name)
        except Beverage.DoesNotExist:
            return HttpResponse("Este producto no existe.")
        else:
            cart.delete_product(product)
            return redirect('beverages')
    else:
        cart.delete_product(product)
        return redirect('pizzas')

def subtract_product(request,product_name):
    cart = Cart(request)
    try:
        product = Pizza.objects.get(name=product_name)
    except Pizza.DoesNotExist:
        try:
            product = Beverage.objects.get(name=product_name)
        except Beverage.DoesNotExist:
            return HttpResponse("Este producto no existe.")
        else:
            cart.subtract_products(product)
            return redirect('beverages')
    else:
        cart.subtract_products(product)
        return redirect('pizzas')

def clean_car(request,product_name):
    cart = Cart(request)
    cart.clean_cart()
    return redirect('pizzas')
    


