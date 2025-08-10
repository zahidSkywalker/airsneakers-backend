from django.urls import path
from .views import (
    ProductListAPI, ProductDetailAPI, CategoryListAPI,
    CheckoutAPI, PaymentSuccessAPI, PaymentFailAPI,
    OrderListAPI, OrderUpdateStatusAPI,
    create_admin_user   # ← added here
)

urlpatterns = [
    path('products/', ProductListAPI.as_view()),
    path('products/<int:pk>/', ProductDetailAPI.as_view()),
    path('categories/', CategoryListAPI.as_view()),
    path('checkout/', CheckoutAPI.as_view()),
    path('payment-success/', PaymentSuccessAPI.as_view()),
    path('payment-fail/', PaymentFailAPI.as_view()),
    path('orders/', OrderListAPI.as_view()),
    path('orders/<int:pk>/', OrderUpdateStatusAPI.as_view()),
    path('create-admin/', create_admin_user),   # ← added here
]
