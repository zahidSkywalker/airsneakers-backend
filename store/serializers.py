from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, source='category', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id','name','slug','description','price','old_price','image_primary','image_secondary','stock','category','category_id']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','customer_name','email','phone','address','items','total_amount','status','tran_id','created_at']
        read_only_fields = ['status','tran_id','created_at']
