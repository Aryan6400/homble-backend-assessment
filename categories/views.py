from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminOrStaffUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
)

from .models import Category
from .serializers import CategorySerializer


# Create your views here.

@api_view(["GET"])
@permission_classes([IsAdminOrStaffUser]) # Using the permission created
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({"categories":serializer.data}, status=HTTP_200_OK)