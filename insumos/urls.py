from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_insumos, name='list_insumos'),
    path('create/', views.create_insumo, name='create_insumo'),
    path('update/<int:pk>/', views.update_insumo, name='update_insumo'),
    path('delete/<int:pk>/', views.delete_insumo, name='delete_insumo'),
]
