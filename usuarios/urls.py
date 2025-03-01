from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),    
    path('profile/update/', views.update_profile, name='update_profile'),
    path('usuarios/', views.list_usuarios, name='list_usuarios'),
    path('usuarios/edit/<int:usuario_id>/', views.edit_usuarios, name='edit_usuarios'),
    path('usuarios/delate/<int:usuario_id>/', views.delate_usuarios, name='delate_usuarios'),
    path('usuarios/create/', views.create_usuarios, name='create_usuarios'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('repartidor/<int:pk>/', views.repartidor_detail, name='repartidor_detail'),
    path('miembro_cuadrilla/<int:pk>/', views.miembro_cuadrilla_detail, name='miembro_cuadrilla_detail'),
    path('administrativo/<int:pk>/', views.administrativo_detail, name='administrativo_detail'),
    
]
