from django.urls import path
from .import views

app_name='seller'

urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add_product,name='add_product'),
    path('catalogue',views.catalogue,name='catalogue'),
    path('cpass',views.change_password,name='change_password'),
    path('orderhistory',views.order_history,name='order_history'),
    path('recentorders',views.recent_orders,name='recent_orders'),
    path('updatestock',views.update_stock,name='update_stock'),
    path('profile',views.profile,name='profile'),


    

]
