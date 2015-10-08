from django.contrib import admin
from core.models import Product, Review, Order


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)