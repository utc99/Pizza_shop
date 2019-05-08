from django.contrib import admin

from .models import Menu, Size, Order, FoodType, PizzaToppingsTypes, MenuPriority, Order_State, PizzaToppings, Single_Order_Item

# Register your models here.


admin.site.register(Menu)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(FoodType)
admin.site.register(PizzaToppingsTypes)
admin.site.register(MenuPriority)
admin.site.register(Order_State)
admin.site.register(Single_Order_Item)
admin.site.register(PizzaToppings)