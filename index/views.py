from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from .forms import CustomerForm , ShippingForm
from .models import *
from .models import Product 



# Create your views here.

def home(request):
    return render(request,'home.html')

def view_products(request):
    context = {'products':Product.objects.all()}
    if request.method=='POST':
        productid = request.POST.get('productid')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(productid)
            if quantity:
             if cart.get(productid,0)<5: 
               cart[productid] = quantity + 1
            
            else:
                cart[productid] = 1
        else:
            cart = {}
            cart[productid] = 1
            
        request.session['cart'] = cart
        print(request.session['cart'])
        return render(request, 'Products.html',context)
    
    return render(request, 'Products.html',context)


def contact_page(request):
        if request.method=='POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request, "Form Is Submitted Succsessfully.")
               print(form)
               return render(request,'contact.html')
            else:
                print(form)
                messages.warning(request, "Account not Found")
                return render(request,'contact.html')
        return render(request, 'contact.html')

def logout_page(request):
    request.session.clear()
    return render(request,'login.html')

def view_products2(request):
    return render(request, '2Product.html')

def productsDetails(request):
    return render(request, 'ProductDetail.html')

def Shopping_cart(request):
     if request.method=='POST':
        productid = request.POST.get('productid')
        remove = request.POST.get('remove')
        cart = request.session.get('cart',{})
    
        if productid is not None and productid.isdigit():
         if cart:
              quantity = cart.get(productid,0)
              if cart.get(productid,0)<5: 
               cart[productid] = quantity + 1
              if remove:
                  cart.pop(productid,None)
              else:
                  quantity=cart.get(productid,None)
         else:
            cart = {productid: 1}
         request.session['cart'] = cart
         
     ids = [int(id) for id in request.session.get('cart',{}).keys() if id.isdigit()]
    #  ids = list(request.session.get('cart',{}).keys())
     products=Product.get_products_by_id(ids)
     return render(request, 'Shoppingcart.html',{'products':products})    

def login_page(request):
    if request.method=="POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            success_message = f"Login successful!\nWelcome, {username}!"
            messages.success(request, success_message)
            request.session['user_id'] = user.id
            user_id = request.session.get('user_id')
            cart=request.session.get('cart',{})
            
            context = {'products':Product.objects.all()}
            
            return render(request ,'Products.html',context)
        else:
            messages.error(request, " incorrect username/password!")
            return render(request, 'login.html')
    return render(request,'login.html')
    
    

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
         messages.error(request, "email/username is already taken!")
         return render(request,'registration.html')
        
        user_obj = User.objects.create(username=username, email=email)
        
        
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "Registration Successful!")
        return render(request,'registration.html')
    
    return render(request, 'registration.html')
    
def YourOrderPage(request):
    return render(request, 'yourorder.html')

def CheckOutPage(request):
    return render(request, 'checkout.html')

def Tracking1Page(request):
    return render(request, 'tracking1.html')

def Tracking2Page(request):
    return render(request, 'tracking1.html')

def Tracking3Page(request):
    return render(request, 'tracking1.html')

def Billing(request):
     if request.method=='POST':
            form = ShippingForm(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request, "submitted")
               return render(request,'Billing-Address.html')
            else:
                messages.warning(request, "not submitted")
                print(form)
                return render(request,'Billing-Address.html')
     return render(request , 'Billing-Address.html')

def payoption(request):
    return render(request , 'payOption.html')

def payGateway(request):
    return render(request , 'payGateway.html')

def upiId(request):
    return render(request , 'upiId.html')




