# Project 3

Web Programming with Python and JavaScript

Requirements
Alright, it’s time to actually build your web application! Here are the requirements:

Menu: Your web application should support all of the available menu items for Pinnochio’s Pizza & Subs (a popular pizza place in Cambridge). It’s up to you, based on analyzing the menu and the various types of possible ordered items (small vs. large, toppings, additions, etc.) to decide how to construct your models to best represent the information. Add your models to orders/models.py, make the necessary migration files, and apply those migrations.
Adding Items: Using Django Admin, site administrators (restaurant owners) should be able to add, update, and remove items on the menu. Add all of the items from the Pinnochio’s menu into your database using either the Admin UI or by running Python commands in Django’s shell.
Registration, Login, Logout: Site users (customers) should be able to register for your web application with a username, password, first name, last name, and email address. Customers should then be able to log in and log out of your website.
Shopping Cart: Once logged in, users should see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping should be saved even if a user closes the window, or logs out and logs back in again.
Placing an Order: Once there is at least one item in a user’s shopping cart, they should be able to place an order, whereby the user is asked to confirm the items in the shopping cart, and the total (no need to worry about tax!) before placing an order.
Viewing Orders: Site administrators should have access to a page where they can view any orders that have already been placed.


User can do all what's required. Admin can see and add/change all items trough admin portal. Additionaly shopping cart content is saved in a session, so it's there after page refresh.
