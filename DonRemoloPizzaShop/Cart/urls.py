from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<str:product_name>/',views.add_product, name = 'add'),
    path('subtract/<str:product_name>/',views.subtract_product, name='subtract'),
    path('delete/<str:product_name>/',views.delete_product, name = 'delete'),
    path('clean/',views.clean_car, name = 'clean'),


]