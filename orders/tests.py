from django.db.models import Max
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Menu, Size, Order, FoodType, PizzaToppingsTypes, MenuPriority, Order_State, PizzaToppings, Single_Order_Item
#from .models import Airport, Flight, Passenger

# Create your tests here.
class MenuTestCase(TestCase):

    def setUp(self):

#Create ITEMS

        # Create foodtypes
        
        f1 = FoodType.objects.create (intype = "Regular Pizza")
        f2 = FoodType.objects.create (intype = "Sicilian Pizza")
        f3 = FoodType.objects.create (intype = "Subs")
        
        # Create sizes
        
        s1 = Size.objects.create (name = "Small", value = "1")
        s2 = Size.objects.create (name = "Regular", value = "2")
        s3 = Size.objects.create (name = "Large", value = "3")
        
        # Create topping_types
        
        tt1 = PizzaToppingsTypes.objects.create (topping_type = "1 topping")
        tt2 = PizzaToppingsTypes.objects.create (topping_type = "2 toppings")
        tt3 = PizzaToppingsTypes.objects.create (topping_type = " ")  
        
        # Create item.
        i1 = Menu.objects.create(food_type=f1, size=s1, toppings_type=tt1, price="13.20", name="1 topping", number_of_toppings="1")
        i2 = Menu.objects.create(food_type=f1, size=s3, toppings_type=tt1, price="17.45", name="1 topping", number_of_toppings="1")
        i3 = Menu.objects.create(food_type=f2, size=s1, toppings_type=tt2, price="27.45", name="2 topping", number_of_toppings="2")
        i4 = Menu.objects.create(food_type=f2, size=s3, toppings_type=tt2, price="41.70", name="2 topping", number_of_toppings="2")
        i5 = Menu.objects.create(food_type=f3, size=s1, toppings_type=tt1, price="6.50", name="Italian", number_of_toppings="1", is_special="2", priority="70")
        i6 = Menu.objects.create(food_type=f3, size=s3, toppings_type=tt1, price="7.95", name="Italian", number_of_toppings="1", is_special="2", priority="80")
        i7 = Menu.objects.create(food_type=f3, size=s3, toppings_type=tt1, price="8.50", name="Sausage, Peppers & Onions", number_of_toppings="1", is_special="2", priority="90")

#CREATE USER
        
        u1 = User.objects.create_user(username='john1', password='john111', is_staff=False)
        #user = authenticate(username="john1", password="john111")
        u1.first_name = "John"
        u1.last_name = "Smith"
        u1.email = "john.smith@gmail.com"
        
        u2 = User.objects.create_user(username='john2', password='john222', is_staff=False)
        #user = authenticate(username="john2", password="john22")
        u2.first_name = "Johny"
        u2.last_name = "Smithers"
        u2.email = "johny.smithers@gmail.com"
        
        
#CREATE ORDERS
        
        # Create Order_State
        
        st1 = Order_State.objects.create(state="Processing", value="1")
        
        # Create Order
        
        o1 = Order.objects.create(state=st1, customer=u1)
        o2 = Order.objects.create(state=st1, customer=u1)
        o3 = Order.objects.create(state=st1, customer=u2)
        
        # Create toppings
        
        t1 = PizzaToppings.objects.create(topping="Ham", group="nogroup")
        t2 = PizzaToppings.objects.create(topping="Mushrooms", group="steak_cheese")
        t3 = PizzaToppings.objects.create(topping="Extra Cheese", group="extra")
        
        # Items in order - Single_Order_Item
    
        so1 = Single_Order_Item.objects.create(order = o1, item = i1, selected_toppings = [t1])
        so2 = Single_Order_Item.objects.create(order = o1, item = i2, selected_toppings = [t2])
        so3 = Single_Order_Item.objects.create(order = o2, item = i5, selected_toppings = [])
        so4 = Single_Order_Item.objects.create(order = o2, item = i5, selected_toppings = t3)
        so5 = Single_Order_Item.objects.create(order = o3, item = i3, selected_toppings = [t1,t2])
        so6 = Single_Order_Item.objects.create(order = o3, item = i4, selected_toppings = [])
        so7 = Single_Order_Item.objects.create(order = o3, item = i7, selected_toppings = [])
        

    def test_items_count(self):
        items = Menu.objects.all()
        self.assertEqual(items.count(), 7)
        
    def test_users_count(self):
        items = User.objects.all()
        self.assertEqual(items.count(), 2)
        
    def test_orders_count(self):
        items = Order.objects.all()
        self.assertEqual(items.count(), 3)
        
    def test_itemsinorder_count(self):
        items = Single_Order_Item.objects.all()
        self.assertEqual(items.count(), 7)        
        
        
