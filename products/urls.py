from django.urls import path

from products.api_endpoints import *


urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name="product-list1"),
    path('list2/', ProductListAPIView2.as_view(), name="product-list2"),
    path('list3/', ProductListAPIView3.as_view(), name="product-list3"),

    path('categories/', CategoryListAPIView.as_view(), name="category-list"),
    path('products/create/', ProductCreateAPIView.as_view(), name="product-create"),
    path('categories/create/', CategoryCreateAPIView.as_view(), name="category-create"),
    path('categories/<str:slug>/', CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    path('categories/<str:slug>/update/', CategoryUpdateAPIView.as_view(), name="category-update"),
    path('categories/<str:slug>/delete/', CategoryDeleteAPIView.as_view(), name="category-delete"),
    path('products/<str:slug>/update/', ProductUpdateAPIView.as_view(), name="product-update"),
    path('products/<str:slug>/delete/', ProductDeleteAPIView.as_view(), name="product-delete"),
]  