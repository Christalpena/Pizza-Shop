from django.db import models

# Create your models here.

class Category(models.Model):
    categories = models.CharField(max_length=30) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category' 
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.categories

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)
    price = models.FloatField()
    image = models.ImageField(upload_to='PizzaImages')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pizza' 
        verbose_name_plural = 'Pizzas'

