from django.shortcuts import render
from common.models import Seller 
from seller.models import Products

# Create your views here.

def home(request):
    # seller = Seller.objects.get(id = request.session ['seller'])
    seller = Seller.objects.filter(id= request.session['seller']).values('seller_name','image')
    seller_name = seller[0]['seller_name']
    seller_pic = seller[0]['image']

    # return render(request,'seller/home.html',{'seller_data':seller})
    return render(request,'seller/home.html',{'name':seller_name,'image':seller_pic })


def add_product(request):

    msg=''
    msg2= ''

    if request.method == 'POST':

        product_name = request.POST['product_name']
        description = request.POST['description']
        price = request.POST['product_price']
        stock = request.POST['product_stock']
        code = request.POST['product_code']
        product_image = request.FILES['product_image']
        

        product_exist = Products.objects.filter(code = code ,seller = request.session['seller']).exists()  #it returns false or true
        if not product_exist:            #(if product_exist == false)

            product = Products(product_name = product_name , description = description , price = price , stock = stock , image = product_image , code = code , seller_id = request.session['seller'])
            product.save()
            msg ='product added successfully'

        else:

            msg2 = 'product is already added'

#product(model_name : view name)
        

    return render(request,'seller/add_product.html',{'product_msg':msg , 'exist_msg': msg2})

def catalogue(request):

    products = Products.objects.filter(seller = request.session['seller'])



    return render(request,'seller/catalogue.html',{'products':products})

def change_password(request):

    error_msg = ''
    success_msg = ''

    if request.method == 'POST':

        old_pass = request.POST['old_password']
        new_pass = request.POST['new_password']
        confirm_pass = request.POST['confirm_password']

        if new_pass == confirm_pass :

            if len(new_pass) >= 8 :

                seller = Seller.objects.get(id = request.session['seller'])

                if seller.password == old_pass :

                    seller.password = new_pass
                    seller.save()
                    success_msg = 'password changed successfully'

                else:
                    error_msg = 'old password is incorrect'

            else:

                error_msg = 'passwords should be 8 characters'


        else:
            error_msg = 'passwords doesn\'t match'

        

    return render(request,'seller/change_password.html',{'success_msg':success_msg,'error_msg':error_msg})

def order_history(request):
    return render(request,'seller/order_history.html')

def recent_orders(request):
    return render(request,'seller/recent_orders.html')

def update_stock(request):
    return render(request,'seller/update_stock.html')

def profile(request):
    return render(request,'seller/profile.html')
