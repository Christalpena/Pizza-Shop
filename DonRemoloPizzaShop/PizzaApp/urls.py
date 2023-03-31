from django.urls import path
from . import views


urlpatterns = [
    path('',views.pizzas, name='pizzas'),
    path('category/<int:id>',views.category,name='category')

]
