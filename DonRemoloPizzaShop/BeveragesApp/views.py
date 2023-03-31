from django.shortcuts import render
from . import models

# Create your views here.

def beverages(request):
    data = models.Beverage.objects.all()
    return render (request,'PizzasApp/pizzas.html',{'data':data})
