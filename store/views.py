from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product, Category, Order
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer
from .payments import initiate_sslcommerz_payment
from .utils import calculate_total
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    pagination_class = None

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CheckoutAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        # calculate total server-side
        items = data.get('items', [])
        try:
            total = calculate_total(items)
        except Exception as e:
            return Response({'error': 'Invalid items or product id'}, status=status.HTTP_400_BAD_REQUEST)
        order_data = {
            'customer_name': data.get('customer_name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'address': data.get('address'),
            'items': items,
            'total_amount': total
        }
        serializer = OrderSerializer(data=order_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        order = serializer.save()
        payment_resp = initiate_sslcommerz_payment(
            order_id=order.id,
            amount=float(order.total_amount),
            customer_name=order.customer_name,
            email=order.email,
            phone=order.phone,
            address=order.address,
        )
        if payment_resp.get('status') in ('SUCCESS','VALID'):
            order.tran_id = payment_resp.get('tran_id') or payment_resp.get('gateway_transaction_id')
            order.save()
        return Response({'order': OrderSerializer(order).data, 'payment': payment_resp})

@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccessAPI(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data
        tran_id = data.get('tran_id') or data.get('tran_id')
        val_id = data.get('val_id')
        try:
            order = Order.objects.get(id=int(tran_id))
            order.status = 'Paid'
            order.tran_id = val_id or order.tran_id
            order.save()
        except Exception:
            pass
        return Response({'received': True})

@method_decorator(csrf_exempt, name='dispatch')
class PaymentFailAPI(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        data = request.data
        tran_id = data.get('tran_id')
        try:
            order = Order.objects.get(id=int(tran_id))
            order.status = 'Cancelled'
            order.save()
        except Exception:
            pass
        return Response({'received': True})

class OrderListAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

class OrderUpdateStatusAPI(views.APIView):
    permission_classes = [permissions.IsAdminUser]
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        status_val = request.data.get('status')
        if status_val not in dict(Order.STATUS_CHOICES):
            return Response({'error': 'Invalid status'}, status=400)
        order.status = status_val
        order.save()
        return Response(OrderSerializer(order).data)
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.http import JsonResponse

