from core.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.ReadOnlyField(source='pk')

    class Meta:
        model = Product
