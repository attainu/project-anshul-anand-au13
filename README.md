Overview: Swiggy (Food Ordering System)

Want a delicious meal, but no time, We will rescue you from the aggression of hunger, we will deliver it hot and yummy. Yummy food which will please you time, money and tummy, Let deliciousness twirl in your mouth.Freshness and happiness on the way...!! you can order from one restaurant at a time.

Project Description :

Design a food ordering system (Swiggy), so that customer should be able to place an order by giving items or restaurant names. Customer can select available restaurants which offers the lowest price for that order item. Should be able to keep track of all items served by each restaurant
and restaurant can also update their menu depending upon the need of the customers. 

Approach and Implementation:

Below listed libraries were imported
• Import TIME - This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.

• created Class restaurant.

• Initially, a List (restaurant) and a List(Dish) was created. 

• Details to perform the tasks “Order and updation", were saved in funtions inside the class.

•.Used Inbuilt datatypes (List) for the database. 

• System can update new food or drink name into the restaurants menu using CLI arguments.

• In a Main function, the operations and data files, resto_data.py and all_tasks.py were imported to perform specific tasks as per the end user need.

• When compiled, customer can search the food name, then the specific item would be displayed from all available restaurants with price inclusive.

• The next available option would be to either proceed with the current order or to decline and look over the menu available. If “order food” was chosen, the system will fetch the food, drinks, service, and discount details from the file. (by creating instance of a class Database_ and calling the function def_full_file_reader()) once the food item was chosen, the system would throw the question to choose the quantity.

• Multiple items can be placed from one restaurant at a time, the maximum quantity to order is 3. Each restaurant has a maximum processing capacity of items at any given time. A list was used to store the number of orders, the system will prompt the customer, whether they need to exit or would like to go with another order.

Future Scope:

• The order confirmation update can be sent to the customer’s email.

• Multiple payment methods can be included for the ease of the customer.
