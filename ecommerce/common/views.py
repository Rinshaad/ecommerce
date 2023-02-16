from django.shortcuts import render,redirect
from .models import Customer,Seller

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def seller_reg(request):

    msg =''

    if request.method == 'POST':
        sname = request.POST['seller_name']
        semail = request.POST['email']
        sphone = request.POST['phone']
        saddress = request.POST['address']
        sgender = request.POST['gender']
        sholder_name = request.POST['holder_name']
        scompany_name = request.POST['company_name']
        sifsc = request.POST['ifsc']
        sbranch = request.POST['branch']
        saccno = request.POST['acc_number']
        # simage = request.FILES['image']

        if 'image' in request.FILES:
            simage = request.FILES['image']

            seller=Seller(seller_name=sname, email=semail, phone=sphone, address=saddress, gender=sgender, holder_name=sholder_name, company_name=scompany_name,branch=sbranch, ifsc=sifsc, account_number=saccno, image=simage )
        else:
            seller=Seller(seller_name=sname, email=semail, phone=sphone, address=saddress, gender=sgender, holder_name=sholder_name, company_name=scompany_name,branch=sbranch, ifsc=sifsc, account_number=saccno )

        seller.save()

        msg = 'You have registered successfully'



    return render(request,'common/seller_reg.html',{'success_msg':msg})

def customer_reg(request):

    msg = ''
    msg2 = ''


    if request.method == 'POST':
        cname = request.POST['customer_name']
        cemail = request.POST['email']
        cphone = request.POST['phone']
        caddress = request.POST['address']
        cgender = request.POST['gender']
        cpassword = request.POST['password']

        email_exist = Customer.objects.filter(email = cemail).exists()

        if email_exist == False:

            customer = Customer(customer_name=cname, email=cemail, phone=cphone, address=caddress, gender=cgender, password=cpassword)
            customer.save()
            
            msg = 'you have registered successfully'


        else:
            msg2 = 'Email is already exist , please use another valid email'


    return render(request,'common/customer_reg.html',{'customer_msg':msg,'exist_msg':msg2})

def seller_login(request):
    msg=''

    if request.method == 'POST':
       
        
        user_name = request.POST['username']
        password = request.POST['password']

        try:
            seller = Seller.objects.get(username = user_name ,password = password)
            request.session['seller'] = seller.id  #seller in quotes is a key
            return redirect('seller:home')   #redirect into home page of seller app

        except Exception as e:
            print(e)
            msg= 'username or password is incorrect!!!'
            

    return render(request,'common/seller_login.html',{'message':msg})

def customer_login(request):

    msg = ''

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        try:
            customer = Customer.objects.get(email = email ,password = password)
            request.session['customer'] = customer.id  
            return redirect('customer:home')   #redirect into home page of seller app

        except Exception as e:
            print(e)
            msg= 'email or password is incorrect!!!'

    return render(request,'common/customer_login.html',{'login_msg':msg})

