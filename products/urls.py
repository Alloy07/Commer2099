from django.urls import path

from products.api_endpoints import *


urlpatterns = [
    path('list1/', ProductListAPIView1.as_view(), name="product-list1"),
    path('list2/', ProductListAPIView2.as_view(), name="product-list2"),
    path('list3/', ProductListAPIView3.as_view(), name="product-list3"),

    path('categories/', CategoryListAPIView.as_view(), name="category-list"),
    path('size/', SizeListAPIView.as_view(), name="size-list"),
    path('brands/', BrandListAPIView.as_view(), name="brand-list"),
    path('colors/', ColorListAPIView.as_view(), name="color-list"),
    path('mediafiles/', MediaFileListAPIView.as_view(), name="media-file-list"),
    path('productVariants/', ProductVariantListAPIView.as_view(), name="product-variant-list"),
    path('products/create/', ProductCreateAPIView.as_view(), name="product-create"),
    path('categories/create/', CategoryCreateAPIView.as_view(), name="category-create"),
    path('brands/create/', BrandCreateAPIView.as_view(), name="brand-create"),
    path('productVariants/create/', ProductVariantCreateAPIView.as_view(), name="product-variant-create"),
    path('colors/create/', ColorCreateAPIView.as_view(), name="color-create"),
    path('size/create/', SizeCreateAPIView.as_view(), name="size-chart-create"),
    path('mediafiles/create/', MediaFileCreateAPIView.as_view(), name="media-file-create"),
    path('categories/<str:slug>/', CategoryRetrieveAPIView.as_view(), name="category-retrieve"),
    path('categories/<str:slug>/update/', CategoryUpdateAPIView.as_view(), name="category-update"),
    path('categories/<str:slug>/delete/', CategoryDeleteAPIView.as_view(), name="category-delete"),
    path('products/<str:slug>/update/', ProductUpdateAPIView.as_view(), name="product-update"),
    path('products/<str:slug>/delete/', ProductDeleteAPIView.as_view(), name="product-delete"),
    path('brands/<str:slug>/update/', BrandUpdateAPIView.as_view(), name="brand-update"),
    path('brands/<str:slug>/delete/', BrandDeleteAPIView.as_view(), name="brand-delete"),
    path('productVariants/<str:slug>/update/', ProductVariantUpdateAPIView.as_view(), name="product-variant-update"),
    path('productVariants/<str:slug>/delete/', ProductVariantDeleteAPIView.as_view(), name="product-variant-delete"),
    path('mediafiles/<str:slug>/update/', MediaFileUpdateAPIView.as_view(), name="media-file-update"),
    path('mediafiles/<str:slug>/delete/', MediaFileDeleteAPIView.as_view(), name="media-file-delete"),
    path('size/<str:slug>/update/', SizeUpdateAPIView.as_view(), name="size-update"),
    path('size/<str:slug>/delete/', SizeDeleteAPIView.as_view(), name="size-delete"),
    path('colors/<str:slug>/update/', ColorUpdateAPIView.as_view(), name="color-update"),
    path('colors/<str:slug>/delete/', ColorDeleteAPIView.as_view(), name="color-delete"),
]  