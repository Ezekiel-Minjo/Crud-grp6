from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='itemList'),
    path('create/', views.item_create, name='itemCreate'),   
    path('update/<int:pk>/', views.item_update, name='itemUpdate'),
    path('delete/<int:pk>/', views.item_delete, name='itemDelete'),
]
    
