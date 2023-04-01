from django.urls import path
from . import views

urlpatterns = [
    path('',views.beverages,name='beverages'),
    path('category/<int:id>',views.category,name='category')

]