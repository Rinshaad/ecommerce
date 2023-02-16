from django.urls import path
from .import views

app_name='ecom_admin'

urlpatterns=[
    path('',views.home,name='home'),
    path('apseller',views.approve_seller,name='approve_seller'),
    path('viewseller',views.view_seller,name='view_seller'),
    path('viewcustomer',views.view_customer,name='view_customer'),

    
    
    


]
