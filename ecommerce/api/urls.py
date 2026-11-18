from django.urls import path 
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('products/', views.product_list_create, name='api-products-list'),
    path('products/<int:pk>/', views.product_detail, name='api-product-detail'),
    path('orders/', views.order_list_create, name='api-order-create'), # <-- Nova rota de pedidos
    path('orders/<int:pk>/status/', views.update_order_status, name='api-order-status')
]