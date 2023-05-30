from django.urls import path
from app_tech_store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/produtos/cadastro', views.admin_add_products, name='add_products'),
    path('admin/produtos/', views.admin_list_products, name='list_products'),
]
