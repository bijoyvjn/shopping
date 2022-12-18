from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('products_listing', products_listing, name='products_listing'),
    path('products_main_listing', products_main_listing, name='products_main_listing'),
    path('add_product', add_product, name='add_product'),
    path('edit_product/<str:pk>', edit_product, name='edit_product'),
    path('product_delete/<str:pk>', product_delete, name='product_delete'),

    path('cart_items/<str:pk>', cart_items, name='cart_items'),
    path('cart', cart, name='cart'),
    path('remove_from/<str:pk>', remove_from, name='remove_from'),
    path('cart_plus/<str:pk>', cart_plus, name='cart_plus'),
    path('cart_minus/<str:pk>', cart_minus, name='cart_minus'),
]
