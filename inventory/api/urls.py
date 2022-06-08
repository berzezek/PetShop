from django.urls import path
from .views import (
    category_list,
    category_detail, 
    category_is_available,

    product_list, 
    product_detail, 
    product_is_available,
    
    order_list,

    cart_list,
    )


urlpatterns = [
    path('categories/', category_list),
    path('category/<int:id>/', category_list),
    path('categoryedit/<int:id>/', category_list),
    path('category_is_available/<int:id>/', category_is_available),
    path('category_detail/<int:id>/', category_detail),
    
    path('products/', product_list),
    path('product/<int:category_id>/', product_list),
    path('productedit/<int:id>/', product_list),
    path('product_is_available/<int:id>/', product_is_available),
    path('product_detail/<int:id>/', product_detail),

    path('orders/<int:cart_id>/', order_list),
    path('order/<int:id>/', order_list),
    path('orderadd/<int:cart_id>/<int:id>/', order_list),

    path('cart/<int:id>/', cart_list),
    path('carts/', cart_list),
]