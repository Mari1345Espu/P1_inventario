from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_productos, name='list_productos'),
    path('create/', views.create_producto, name='create_producto'),
    path('update/<int:pk>/', views.update_producto, name='update_producto'),
    path('delete/<int:pk>/', views.delete_producto, name='delete_producto'),
    path('bodegas/', views.list_bodegas, name='list_bodegas'),
    path('bodegas/create/', views.create_bodega, name='create_bodega'),
    path('bodegas/update/<int:pk>/', views.update_bodega, name='update_bodega'),
    path('bodegas/delete/<int:pk>/', views.delete_bodega, name='delete_bodega'),
    path('add_carrito/<int:producto_id>/', views.add_carrito, name='add_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('remove_carrito/<int:producto_id>/', views.remove_carrito, name='remove_carrito'),
    path('increase_quantity/<int:producto_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:producto_id>/', views.decrease_quantity, name='decrease_quantity'),
    
]
