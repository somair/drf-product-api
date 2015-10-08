from core.models import Product
from rest_framework import viewsets
from api import serializers


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or created.
    """
    queryset = Product.objects.all()
    paginate_by = 2

    serializer_class = serializers.ProductSerializer
