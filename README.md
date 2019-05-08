# Project 3

Web Programming with Python and JavaScript




user
{% extends "orders/base.html" %}

{% block body %}
<h1>LOGGED IN Hello, {{ user.first_name }}</h1>
<ul>
    <li>Currently logged in as: {{ user.username }}</li>
    <li><a href="{% url 'logout' %}">Logout</a></li>
</ul>

<table style="width:100%">
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>

    <h1>Menu1</h1>
   <!-- {% regroup menu|dictsort:"price"|dictsortreversed:"menu_priority" by food_type as menugrouped %} -->
    {% regroup menu|dictsort:"price" by food_type as menugrouped %}

    {% for type in menugrouped %}
    <li>{{menugrouped}}</li>
        {% if "Regular" == type.grouper|stringformat:"s" or "Sicilian" == type.grouper|stringformat:"s"%}
            <h2 id=food_type_header>{{type.grouper}} Pizza</h2>
        {% endif %} 
        {% if "Regular" != type.grouper|stringformat:"s" and "Sicilian" != type.grouper|stringformat:"s"%}
            <h2 id=food_type_header>{{type.grouper}} </h2>
        {% endif %} 
        
        <table style="width:100%">
        
      {% regroup type.list by toppings_type as toppingsdmenu %} 
      
  {% for item in toppingsdmenu %}
       <tr>       
       {% for item in item.list %}
            
            {% if "Large" != item.size|stringformat:"s" %}
                <td>{{item.toppings_type}}</td>
                <td>{{item.price}}</td>
            {% endif %} 
            
            {% if "Large" == item.size|stringformat:"s" %}
                <td>{{item.price}}</td>
            {% endif %}
        {% endfor %} 
        </tr>
  {% endfor %}
  
        </table>
  
 <!--       {% for item in type.list|dictsort:"price" %}
        {{item.toppings}}
            <li>
                {{item}}
            </li>
        {% endfor %}
-->        
    {% endfor %}
{% endblock %}
