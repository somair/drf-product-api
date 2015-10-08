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

product_review = views.ProductReviewViewSet.as_view({
    'get': 'list',
})

order_detail = views.OrderViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'product/$', product_list, name='product-list'),
    url(r'product/(?P<pk>[0-9]+)/$', product_detail, name='product-detail'),
    url(r'product/(?P<pk>[0-9]+)/reviews/$', product_review, name='product-reviews'),
    url(r'review/$', review_list, name='review-list'),
    url(r'review/(?P<pk>[0-9]+)/$', review_detail, name='review-detail'),
    url(r'order/(?P<pk>[0-9]+)/$', order_detail, name='order-detail'),
]
