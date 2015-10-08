from core.models import Product, Review
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.ReadOnlyField(source='pk')

    class Meta:
        model = Product


class ProductListSerializer(ProductSerializer):

    class Meta:
        model = Product
        fields = ('product_id', 'name', 'url')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    review_id = serializers.ReadOnlyField(source='pk')

    class Meta:
        model = Review


class ReviewListSerializer(ReviewSerializer):

    class Meta:
        model = Review
        fields = ('review_id', 'url')


class ReviewPostSerializer(serializers.ModelSerializer):
    """
    Use this serializer for POST as there is a requirement with the hyperlinked modelserializer to pass the full URL
    rather than the product id.
    """
    class Meta:
        model = Review
