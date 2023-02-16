from django.shortcuts import render,redirect
from seller.models import Products
from common.models import Customer
from customer.models import Cart

# Create your views here.


def home(request):
    return render(request,'customer/home.html')
def cart(request):
    cart = Cart.objects.filter(customer = request.session['customer'])

    return render(request,'customer/cart.html',{'cart':cart})
def orders(request):
    return render(request,'customer/orders.html')
def products(request):

    products = Products.objects.all()
    return render(request,'customer/products.html',{'products': products})
    
def changepassword(request):


    error_msg = ''
    success_msg = ''

    if request.method == 'POST':

        old_pass = request.POST['old_password']
        new_pass = request.POST['new_password']
        confirm_pass = request.POST['confirm_password']

        if new_pass == confirm_pass :

            if len(new_pass) >= 8 :

                customer = Customer.objects.get(id = request.session['customer'])

                if customer.password == old_pass :

                    # customer.password = new_pass
                    # customer.save()

                    Customer.objects.filter(id = request.session['customer']).update( password = new_pass )
                    success_msg = 'password changed successfully'

                else:
                    error_msg = 'old password is incorrect'

            else:

                error_msg = 'passwords should be 8 characters'


        else:
            error_msg = 'passwords doesn\'t match'

    return render(request,'customer/changepassword.html',{'success_msg':success_msg,'error_msg':error_msg})
def profile(request):
    return render(request,'customer/profile.html')

def product_details(request,pid):
    error_msg = ''

    product = Products.objects.get( id = pid )

    if request.method == 'POST':
        customer = request.session['customer']   #getting customer id from session

        record_exist = Cart.objects.filter( product = pid ,customer = customer ).exists()

        if record_exist == False:  # if not record_exist

            cart = Cart(customer_id = customer ,product_id = pid)
            cart.save()
            return redirect('customer:cart')


        else:

            error_msg = 'item already in cart'


        

    return render(request,'customer/product_details.html',{'product_details':product , 'message':error_msg})