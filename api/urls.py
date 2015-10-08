from django.conf.urls import url
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)

product_detail = views.ProductViewSet.as_view({
    'get': 'retrieve'
})

product_list = views.ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

review_detail = views.ReviewViewSet.as_view({
    'get': 'retrieve'
})

review_list = views.ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    url(r'product/$', product_list, name='product-list'),
    url(r'product/(?P<pk>[0-9]+)/$', product_detail, name='product-detail'),
    url(r'review/$', review_list, name='review-list'),
    url(r'review/(?P<pk>[0-9]+)/$', review_detail, name='review-detail'),
]
