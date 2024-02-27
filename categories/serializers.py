from rest_framework import serializers
from categories.models import Category
from products.models import Product
from products.serializers import ProductListSerializer


class CategorySerializer(serializers.ModelSerializer):
    """
    To show list of categories.
    """
    products = serializers.SerializerMethodField()
    count_products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id','name','is_active','count_products','products']
    
    # To get the products for the category
    def get_products(self, obj):
        products = obj.products.all()
        serializer = ProductListSerializer(products, many=True)
        return serializer.data
    
    # To get the count of products in each category dynamically
    def get_count_products(self, obj):
        return obj.products.count()
