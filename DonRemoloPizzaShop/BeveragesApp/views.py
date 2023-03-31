from django.shortcuts import render
from . import models

# Create your views here.

def beverages(request):
    data = models.Beverage.objects.all()
    ctg = models.Category.objects.all()
    return render (request,'BeverageApp/beverage.html',{'data':data,'ctg':ctg})

def category(request,id):
    data = models.Category.objects.get(id = id)
    data = models.Beverage.objects.filter(category = data)
    ctg = models.Category.objects.all()
    return render(request,'BeverageApp/beverage.html',{'data':data,'ctg':ctg})
