from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index-page'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<slug:category_slug>/', ProductsListView.as_view(), name='products-list'),
    path('products/details/<int:pk>/', ProductDeatilsView.as_view(), name='product-details'),
    path('products/edit/<int:pk>/', ProductEditView.as_view(), name='product-edit'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),

]

