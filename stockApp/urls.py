from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,BrandViewSet
from . import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('category/search/', views.category_search, name='category_search'),
    path('category/filter/', views.category_filter, name='category_filter'),
    path('sale/search/', views.sale_search, name='sale_search'),
    path('sale/filter/', views.sale_filter, name='sale_filter'),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('brand/search/', views.brand_search, name='brand_search'),
    path('purchase/search/', views.purchase_search, name='purchase_search'),
    path('purchase/filter/', views.purchase_filter, name='purchase_filter'),

]
