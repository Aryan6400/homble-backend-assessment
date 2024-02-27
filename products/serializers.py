from rest_framework import serializers

from products.models import Product, SKU

# To nest SKUs in product object to provide full details of the product
class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model=SKU
        fields=('size','selling_price')

class ProductListSerializer(serializers.ModelSerializer):
    """
    To show list of products.
    """
    skus = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "description", "ingredients", "is_refrigerated", "category", "managed_by", "skus")

    def get_skus(self, obj):
        skus = SKU.objects.filter(product=obj)
        serializer = SKUSerializer(skus, many=True)
        return serializer.data