from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
)

from .models import Product
from .serializers import ProductListSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def products_list(request):
    """
    List of all products.
    """

    is_refrigerated=request.query_params.get("isRefrigerated")
    if(is_refrigerated!=None):
        is_refrigerated=is_refrigerated.lower() # To consider cases when user enters true and True, both should return correct response.
        
    # For any keyword other than true and false(in any casing), API won't return an error but all the products. Or we can also raise error for invalid query.

    if is_refrigerated=="true":
        products = Product.objects.filter(is_refrigerated=True)
    elif is_refrigerated=="false":
        products = Product.objects.filter(is_refrigerated=False)
    else:
        products = Product.objects.all()
    
    print(products)
    serializer = ProductListSerializer(products, many=True)
    return Response({"products": serializer.data}, status=HTTP_200_OK)
