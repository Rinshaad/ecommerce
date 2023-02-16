from django.shortcuts import render
from common.models import Seller
from django.core.mail import send_mail
from random import randint
from django.conf import settings 


# Create your views here.



def home(request):
    return render(request,'ecom_admin/home.html')

def approve_seller(request):

    sellers = Seller.objects.filter(status ='pending')

    if request.method == 'POST':
        seller_id= request.POST['seller_id']
        seller = Seller.objects.get(id = seller_id)

        if 'approve' in request.POST:
            #login when approve button clicked
            user_name = randint(1111,9999)
            password = 'sel-' + str(user_name) + str(seller.phone)[:5]
            
            seller.status = 'approved' #sql update query
            seller.username = user_name
            seller.password = password
            seller.save()

            #setting type of username,password and message

           
            mail_subject = 'Account Approval'
            message_body = 'Hi your account has been approved by admin , you can now login with username ' +str(user_name)+ 'and temporary password '+ password

            
        if 'reject' in request.POST:
            
            seller.status = 'rejected' 
            seller.save()

            
            mail_subject = 'Account Rejected'
            message_body = 'sorry your account has been rejected by admin '


        send_mail(
                subject=mail_subject,
                message=message_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[seller.email]
            )

    return render(request,'ecom_admin/approve_seller.html',{ 'sellers_list' : sellers  })

def view_seller(request):

    seller =Seller.objects.filter(status='approved')

    return render(request,'ecom_admin/view_seller.html',{'seller_list' : seller})

def view_customer(request):
    return render(request,'ecom_admin/view_customer.html')
