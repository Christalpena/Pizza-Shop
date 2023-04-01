from django.http import HttpResponse
from django.shortcuts import render,redirect
from BeveragesApp.models import Beverage
from PizzaApp.models import Pizza
from .cart import Cart
from .forms import Information
from django.core.mail import EmailMessage
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

def form(request,path):
    form = Information()
    if request.method == 'POST':
        form = Information(request.POST)
        if form.is_valid():
            user_email = request.POST.get('Gmail')
            cart = Cart(request)
            data = cart.Product_list()
            for data in data:
                data = "{} \n".format(data)

            email = EmailMessage(
                "ORDER FROM PIZZA_APP",
                "From: {} \n ORDER: {}".format(user_email,data),"",
                ['penaperezchristal@gmail.com'],
                reply_to=[user_email]
            )
            try:
                email.send()
                if path == "/pizzas/":
                    return redirect ("/pizzas/?valid")
                else:
                    return redirect ("/Beverages/?valid")

            except:
                if path == '/pizzas/':
                    return redirect ("/pizzas/?something_Went_Wron")
                else:
                    return redirect ("/Beverages/?something_Went_Wron")
    return render(request,'cart/form.html',{"form":form})











    


