from django.urls import path
from .import views

app_name='common'

urlpatterns=[
    path('',views.home,name='home'),
    path('clogin',views.customer_login,name='customer_login'),
    path('slogin',views.seller_login,name='seller_login'),
    path('creg',views.customer_reg,name='customer_reg'),
    path('sreg/',views.seller_reg,name='seller_reg'),


]
