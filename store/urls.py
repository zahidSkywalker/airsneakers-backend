from django.urls import path
from .views import (
    ProductListAPI, ProductDetailAPI, CategoryListAPI,
    CheckoutAPI, PaymentSuccessAPI, PaymentFailAPI,
    OrderListAPI, OrderUpdateStatusAPI
)

urlpatterns = [
    path('products/', ProductListAPI.as_view(), name='api-products'),
    path('products/<int:id>/', ProductDetailAPI.as_view(), name='api-product-detail'),
    path('categories/', CategoryListAPI.as_view(), name='api-categories'),
    path('checkout/', CheckoutAPI.as_view(), name='api-checkout'),
    path('payment/success/', PaymentSuccessAPI.as_view(), name='payment-success'),
    path('payment/fail/', PaymentFailAPI.as_view(), name='payment-fail'),
    path('orders/', OrderListAPI.as_view(), name='api-orders'),
    path('orders/<int:pk>/status/', OrderUpdateStatusAPI.as_view(), name='api-order-status'),
]
