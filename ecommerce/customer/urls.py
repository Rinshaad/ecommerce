from django.urls import path
from .import views

app_name='customer'

urlpatterns=[
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('orders',views.orders,name='orders'),
    path('products',views.products,name='products'),
    path('profile',views.profile,name='profile'),
    path('product/<int:pid>',views.product_details,name='product_details'),


    



]
