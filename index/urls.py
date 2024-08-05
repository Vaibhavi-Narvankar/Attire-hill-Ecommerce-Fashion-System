# added manually from projects urls.py

from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path("", views.home , name='home'),
    path("home", views.home , name='home'),
    path("Products",views.view_products, name='product'),
    path("contact",views.contact_page, name='conatct'),
    path("login",views.login_page, name='login'),
    path("registration",views.register_page, name='register'),
    path("2Product",views.view_products2, name='product1'),
    path("ProductDetail",views.productsDetails, name='productDetails'),
    path("Shoppingcart",views.Shopping_cart, name='shoppingCart'),
    path("login",views.login_page,name='login'),
    path('yourorder',views.YourOrderPage,name='order'),
    path("checkout",views.CheckOutPage,name='checkout'),
    path("tracking1",views.Tracking1Page,name="tracking1"),
    path("tracking2",views.Tracking2Page,name="tracking2"),
    path("tracking3",views.Tracking3Page,name="tracking3"),
    path("logout",views.logout_page,name='logout'),
    path("Billing-Address",views.Billing,name='billing'),
    path("payOption",views.payoption,name='payoption'),
    path("payGateway",views.payGateway,name='payGateway'),
    path("upiId",views.upiId,name='upiId'),
   
    
    
]
