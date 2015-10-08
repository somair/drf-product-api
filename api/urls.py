from django.conf.urls import url
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)

product_detail = views.ProductViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'product/(?P<pk>[0-9]+)/$', product_detail, name='product-detail'),
]
