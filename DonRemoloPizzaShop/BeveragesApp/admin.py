from django.contrib import admin
from . import models

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    readonly_fields = ('created','updated')

admin.site.register(models.Category,CategoriesAdmin)
admin.site.register(models.Beverage,BeverageAdmin)