from django.shortcuts import render
from . import models

# Create your views here.

def pizzas(request):
    data = models.Pizza.objects.all()
    return render (request,'PizzasApp/pizzas.html',{'data':data})
