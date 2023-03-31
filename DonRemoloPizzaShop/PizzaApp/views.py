from django.shortcuts import render
from . import models

# Create your views here.

def pizzas(request):
    data = models.Pizza.objects.all()
    ctg = models.Category.objects.all()

    return render (request,'PizzasApp/pizzas.html',{'data':data,'ctg':ctg})

def category(request,id):
    data = models.Category.objects.get(id = id)
    data = models.Pizza.objects.filter(category = data)
    ctg = models.Category.objects.all()
    return render(request,'PizzasApp/pizzas.html',{'data':data,'ctg':ctg})