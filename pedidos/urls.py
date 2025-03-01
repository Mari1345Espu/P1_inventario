from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_pedidos, name='list_pedidos'),
    path('create/', views.create_pedido, name='create_pedido'),
    path('update/<int:pk>/', views.update_pedido, name='update_pedido'),
    path('delete/<int:pk>/', views.delete_pedido, name='delete_pedido'),
    path('detalles/<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('solicitudes/', views.list_solicitudes_cotizacion, name='list_solicitudes_cotizacion'),
    path('solicitudes/create/', views.create_solicitud_cotizacion, name='create_solicitud_cotizacion'),
    path('solicitudes/update/<int:pk>/', views.update_solicitud_cotizacion, name='update_solicitud_cotizacion'),
    path('solicitudes/delete/<int:pk>/', views.delete_solicitud_cotizacion, name='delete_solicitud_cotizacion'),
    path('solicitudes/detalles/<int:pk>/', views.detalle_solicitud_cotizacion, name='detalle_solicitud_cotizacion'),
]
