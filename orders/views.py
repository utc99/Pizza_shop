from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse

from .models import Menu, Size, Order, FoodType, PizzaToppingsTypes, MenuPriority, Order_State, PizzaToppings, Single_Order_Item

# Create your views here.

#Global variable for price update when "SUBS" with pricing per topping are selected
updated_price = '0.00'

#Index page - authenticated and not
def index(request):
    
    if request.user.is_authenticated:
        
        context = {
        "user": request.user,
        "menu": Menu.objects.all(),
        "toppings": PizzaToppings.objects.all()
        }
        
        return render(request, "orders/home.html", context)
        
    context = {
        "menu": Menu.objects.all(),
        "message": None,
        "toppings": PizzaToppings.objects.all()
    }
    return render(request, "orders/index.html", context)

#Login
def login_view(request):
    
    username = request.POST["username"]
    password = request.POST["password"]
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        context = {
            "menu": Menu.objects.all(),
            "message": "Invalid credentials.",
            "toppings": PizzaToppings.objects.all()
        }
        return render(request, "orders/index.html", context)

#Logout
def logout_view(request):
    
    logout(request)
    context = {
            "menu": Menu.objects.all(),
            "message": "Logged Out",
            "toppings": PizzaToppings.objects.all()
        }
    return render(request, "orders/index.html", context)

#New user's registration
def register(request):
    
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
        
            userinfo = form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            userinfo.first_name = request.POST.get("first_name")
            userinfo.last_name = request.POST.get("last_name")
            userinfo.email = request.POST.get("email")
            
            userinfo.save()
            login(request, user)
            
            return redirect('index')
        
        context = {
            "message": form.errors,
            "menu": Menu.objects.all(),
            "toppings": PizzaToppings.objects.all()
        }
        return render(request, "orders/index.html", context)
        
    else:
        context = {
            "message": "GET method not supported",
            "menu": Menu.objects.all(),
            "toppings": PizzaToppings.objects.all()
        }
        return render(request, "orders/index.html", context)
    
#Show user's orders    
#Admin sees all orders
def myorders(request):

    if request.user.is_superuser:
        all_User_orders = Order.objects.all()
    else:
        all_User_orders = Order.objects.filter(customer=request.user.id)
    
    context = {
        "orders": all_User_orders
    }
    
    return render(request, "orders/order.html", context)    
    
# Buy items in a USER's shopping cart.    
def buy(request):
    
    cart_valid = True
    
    try:
        user = request.user
        data = json.loads(request.body)
    except KeyError:
        return JsonResponse({"status": "Purchase cannot be completed. BUY status Code 01. Contact administrator."})
    
    s = Order_State.objects.get(state="Processing")
    new_order = Order(state = s, customer = user)
    new_order.save()
    
    order_id = new_order.id
    
    for item in data['cart']:
        
        toppings = item['toppings']
        cart_valid = cart_validation(item, toppings)
        
        if (cart_valid):
            
            i = Menu.objects.get(pk=item['id'])
            i.price = updated_price
            new_item = Single_Order_Item(order = new_order, item = i, selected_toppings = toppings)
            new_item.save()
    
    if (cart_valid):
        return JsonResponse({"status": "Success"})    
        
    else:
        Order.objects.filter(pk=order_id).delete()
        return JsonResponse({"status": "Purchase cannot be completed. BUY status Code 02. Contact administrator."})
    
    return JsonResponse({"status": "Unknown state. BUY status Code 03. Contact administrator."})
    
# Check if all items in the USER's shopping cart exists and prices are correct. 
# Mixed in  - if an item is from "SUBS" and so has per topping pricing, calculate updated price
def cart_validation(item, toppings):
    
    global updated_price
    
    if not Menu.objects.filter(pk=item['id']).exists():
        cart_valid = False
        return False
        
    else:
        i = Menu.objects.filter(pk=item['id'])
        item_price = i[0].price
        updated_price = item_price
        
        if str(i[0].food_type) == "Subs":
            for topping in toppings:
                item_price = float(item_price) + 0.50
                item_price = "{:.2f}".format(item_price)
                updated_price = item_price

        if str(item_price) == item['price']:
            return True
            
        else: 
            cart_valid = False
            return False
        