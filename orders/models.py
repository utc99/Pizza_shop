from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

    
# Create your models here.

class Single_Order_Item(models.Model):
    order = models.ForeignKey("Order", related_name="in_order", on_delete=models.CASCADE)
    item = models.CharField(max_length=128, default="")
    selected_toppings = models.CharField(max_length=128, default="None")
    
    def __str__(self):
        return f"{self.order} - {self.item} - {self.selected_toppings}"            


class Size(models.Model):
    name = models.CharField(max_length=64)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class Order_State(models.Model):
    state = models.CharField(max_length=64)
    value = models.IntegerField()
    
    def __str__(self):
        return f"{self.state}" 
        
class FoodType(models.Model):
    intype = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.intype}" 

class PizzaToppingsTypes(models.Model):
    topping_type = models.CharField(max_length=64, blank=True, default="")

    def __str__(self):
        return f"{self.topping_type}"         

class MenuPriority(models.Model):
    name = models.CharField(max_length=64)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.name}"     
        
class Menu(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name="items")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="items")
    toppings_type = models.ForeignKey(PizzaToppingsTypes, on_delete=models.CASCADE, related_name="items", blank=True, default=6)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    priority = models.IntegerField(default=50);
    name = models.CharField(max_length=64)
    number_of_toppings = models.IntegerField(default=0);
    is_special = models.IntegerField(default=0)
    comment = models.CharField(max_length=64, blank=True)
    show = models.BooleanField(default=True)
    
    def __str__(self):
        return f" {self.food_type} - {self.name} - {self.size} for {self.price} USD."
        
    class Meta:
        ordering = ['food_type', 'toppings_type', 'size']

class Order(models.Model):
    state = models.ForeignKey(Order_State, on_delete=models.PROTECT, related_name="orders", default=2 )
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Date: {self.created_at.strftime('%Y-%m-%d %H:%M')}. Order #:{self.id}. State: {self.state}. Customer: {self.customer.email}"

def get_first_name(self):
    info = self.username + " " + self.first_name + " " + self.last_name
    return info

class PizzaToppings(models.Model):
    topping = models.CharField(max_length=64, blank=False)
    group = models.CharField(max_length=64, default="nogroup")

    def __str__(self):
        return f"{self.topping}"  

User.add_to_class("__str__", get_first_name)        