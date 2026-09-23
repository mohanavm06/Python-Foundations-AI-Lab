# Mohana

# Lesson Five

# Lab 5 - Collections in Python



# Scenario

# You have been asked to build a flexible order management system for a small online store.

# The system must handle customers, products and orders. Different orders may contain different numbers of

# products and different optional information.

# Your goal is to design the program using functions and the concepts covered in Lesson 5.

# Unlike the standard lab, you will not be told exactly where to use every Python feature. You are expected to

# decide when *args, **kwargs, unpacking and different types of parameters are appropriate.

# Your program should also demonstrate that you understand variable scope.



# Part 1 - Products and customers

# Create data for at least:

# • 8 products

# • 5 customers

# Each product should contain information such as:

# • product name

# • price

# • category

# Each customer should contain at least:

# • name

# • email

# • customer ID

# You decide how to structure the data using concepts from previous lessons.



products = [

  {

    "product_id": "P001",

    "name": "Trådlösa hörlurar",

    "price": 899,

    "category": "Ljud",

  },

  {

    "product_id": "P002",

    "name": "Bluetooth-högtalare",

    "price": 599,

    "category": "Sonos",

  },

  {

    "product_id": "P003",

    "name": "keyboard mechanical",

    "price": 1299,

    "category": "Datortillbehör",

  },

  {

    "product_id": "P004",

    "name": "Ergonomisk mus",

    "price": 449,

    "category": "Datortillbehör",

  },

  {

    "product_id": "P005",

    "name": "USB-C-hubb",

    "price": 349,

    "category": "Computer accessories",

  },

  {"product_id": "P006", "name": "Skrivbordslampa", "price": 799, "category": "Hem"},

  {"product_id": "P007", "name": "Kaffebryggare", "price": 1499, "category": "Hem"},

  {"product_id": "P008", "name": "Ryggsäck 20L", "price": 699, "category": "Väskor"},

]



customers = [

  {

    "customer_id": "C001",

    "name": "Anna Andersson",

    "email": "anna.andersson@example.se",

  },

  {

    "customer_id": "C002",

    "name": "Sam Simon",

    "email": "sam_simon@example.se",

  },

  {"customer_id": "C003", "name": "Carla Chen", "email": "carla.chen@example.se"},

  {"customer_id": "C004", "name": "David Dahl", "email": "david.dahl@example.se"},

  {"customer_id": "C005", "name": "Eva Eklund", "email": "eva.eklund@example.se"},

]



example_settings = {

  "shipping": "standard",

  "gift_message": "Thank for help!",

  "campaign": "HOST26",

  "delivery_instructions": None,

  "priority": False,

}



# Part 2 - Create orders

# Create a function for creating an order.

# An order must contain:

# • order ID

# • customer

# • one or more products

# However, an order may also contain optional information such as:

# • shipping method

# • discount

# • priority

# • gift message

# • delivery instructions

# • campaign code

# Your function should be flexible enough to accept different amounts of optional information without requiring

# every possible option to be defined beforehand.

# The function should return a structured representation of the order.

# Create at least five different orders with different products and optional information.



next_order_number = 100100





def generate_order_id():

  global next_order_number

  order_id = f"ORDER-{next_order_number}"

  next_order_number += 1

  return order_id





def find_customer(customer_id):

  for customer in customers:

    if customer["customer_id"] == customer_id:

      return customer





def find_product(product_id):

  for product in products:

    if product["product_id"] == product_id:

      return product





def create_order(customer_id, *product_ids, **options):

  order_products = []

  for product_id in product_ids:

    order_products.append(find_product(product_id))



  return {

    "order_id": generate_order_id(),

    "customer": find_customer(customer_id),

    "products": order_products,

    "options": options,

  }





order1 = create_order("C001", "P001", "P003", **example_settings)



order2 = create_order("C002", "P007", shipping="express", priority=True)



cart = ["P002", "P004", "P005"]

order3 = create_order("C003", *cart, discount=10)



gift_settings = {"gift_message": "Congratulations on your birthday!", "shipping": "standard"}

order4 = create_order("C004", *["P006", "P008"], **gift_settings, campaign="HOST26")



order5 = create_order("C005", "P005")



orders = [order1, order2, order3, order4, order5]



# Part 3 - Variable number of products

# Customers can purchase any number of products in one order.

# Create a function that can receive a variable number of product prices and calculate the subtotal.

# For example, your function should work conceptually with:

# calculate_subtotal(199)

# as well as:

# calculate_subtotal(199, 349, 99, 129)

# Do not create separate functions for different numbers of products.

# Your function must also handle the situation where no prices are supplied.





def calculate_subtotal(*prices):

  return sum(prices)





print(calculate_subtotal(199))

print(calculate_subtotal(199, 349, 99, 129))

print(calculate_subtotal())



for order in orders:

  prices = [product["price"] for product in order["products"]]

  subtotal = calculate_subtotal(*prices)

  print(f"{order['order_id']}: {subtotal} kr")





# Part 4 - Order configuration

# Create a function that receives optional order settings. Different orders may provide different settings.

# For example:

# shipping="express"

# priority=True

# discount=10

# while another order might provide:

# shipping="standard"

# gift_message="Happy birthday!"

# Your function should process the supplied settings and return them in a useful structure.

# Optional settings whose value is None should not be included in the final result.





def configure_order(**settings):

  configuration = {}

  for key, value in settings.items():

    if value is not None:

      configuration[key] = value

  return configuration





config1 = configure_order(shipping="express", priority=True, discount=10)

config2 = configure_order(shipping="standard", gift_message="Happy birthday!")

config3 = configure_order(**example_settings)



print(config1)

print(config2)

print(config3)



# Part 5 - Unpacking existing data

# Some customer and product information already exists in collections.

# Create examples where you use existing:

# • lists or tuples as positional arguments

# • dictionaries as keyword arguments

# Instead of manually writing every argument again, unpack the existing data when calling your functions.

# Demonstrate at least:

# • two examples using positional unpacking

# • two examples using dictionary unpacking

# At least one dictionary should contain all the information required to call one of your existing functions.



# Part 6 - Flexible order summary

# Create a function that produces a readable order summary.

# The function should accept:

# • an order ID

# • a customer

# • a variable number of messages or notes

# • optional metadata

# Example usage could conceptually look like:

# order_summary(

# "ORD-1042",

# "Anna Andersson",

# "Express delivery",

# "Leave at reception",

# priority=True,

# campaign="SUMMER26"

# )

# 1

def merge_settings(defaults, **overrides):

  return {**defaults, **overrides}





defaults = {"theme" : "light", "font_size" : 12, "autosave" : True, "language" : "en"}

result_1 = merge_settings(defaults, theme="dark", font_size=16)

print(result_1)

print(defaults)



# Part 7

# 2

def call_summary(function_name, *args, **kwargs):

  named_args = []

  for item in args:

    named_args.append(f"{item!r}") # conversion field calls repr() - just shows how you'd type the value like quote marks on string

  for k, v in kwargs.items():

    named_args.append(f"{k}={v!r}")

  named_args = ", ".join(named_args)

  return f"{function_name}({named_args})"





output = call_summary("submit_attendance", "Harry Potter", True, platform="attendance_portal", retries=3, report_webpage_error=True)

print(output)



output = call_summary("register_course", "Ron Weasley", False, platform="Udemy", retries=0, report_webpage_error=False)

print(output)





# 3

def statistics(*numbers):

  if not numbers:

    return "No Numbers were provided", 0, 0, 0 ,0

  else:

    count = 0

    total = 0

    min_val = numbers[0]

    max_val = numbers[0]

    for n in numbers:

      count += 1

      total += n

      if n < min_val:

        min_val = n

      elif n > max_val:

        max_val = n

    average = total / count

  return count, total, average, min_val, max_val





count, total, average, min_val, max_val = statistics(1, 5, 3, 7, 9, 2, 4)

print(f"Count : {count} \nTotal : {total} \nAverage : {average:.2f} \nMin Value : {min_val} \nMax Value : {max_val}")



count, total, average, min_val, max_val = statistics()

print(f"\nCount : {count} \nTotal : {total} \nAverage : {average:.2f} \nMin Value : {min_val} \nMax Value : {max_val}")







# 4



print("Predict 1")

message = "This is global"

def msg():

  message = "This is local"

  print(message)



msg()

print(message)

print("Prediction: assigning inside msg() creates a new local, and global is untouched")



print("Predict 2")

count = 5

# def counter():

#   count = count + 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value

#   return count



# print(counter())

print(count)

print("Prediction : UnBoundLocalError ")





print("Predict 3")

name = "Harry"

def username():

  namess = "This is local"



  def innerLoop():

    print(f"inner loop : {name}")

    print(names)

  names = "test"

  innerLoop()

  print(name)



username()

print(name)



# note : global variables can be accessed without global keyword inside function

# but need to use global keyword to modify it



print("Predict 4")

def username():

  def innerLoop():

    print("inner sees:", names)

  names = "first"

  innerLoop()     # inner sees: first

  names = "second"

  innerLoop()     # inner sees: second

username()





print("Predict 5")

# squares = [x * x for x in range(3)]

# print(x)       # NameError: name 'x' is not defined





print("Predict 6")

for i in range(3):

  pass

print(i)



if True:

  colour = "red"

print(colour)



# if False:

#   colour = "red"

# print(colour)   # NameError: name 'colour' is not defined 



print("""

Prediction :

- variables created inside for, if, while can be accessed outside only if it ran, i.e., the line that creates the variable has to actually run.

- functions create a new scope

- list or any other iterable comprehension creates a new scope

""")

# part 7 Scope and order statistics

# • reading a global variable from inside a function
# • creating a local variable with the same name
# • attempting to assign to a global numeric variable inside a function
# Do not use global simply to make the code work.
# Instead, redesign the function so that it returns the new value, and update the variable outside the
# function.
# Add comments explaining why this approach is preferable.
# Also create one small example demonstrating an enclosing scope using a nested function.
# Part 8 - Order processing
# Create a function that processes an order.
# It should receive some required information explicitly, while also supporting:
# • a variable number of products
# • optional order settings
# The function should calculate and return useful information such as:
# • subtotal
# • discount
# • shipping cost
# • final total
# Think carefully about which parameters should be explicitly named and which information actually benefits
# from flexible arguments.
# Do not use *args or **kwargs simply because they are available.
# Your parameter design should make sense.
# Part 9 - Different order types
# Use your system to create and process at least:
# • one order containing one product
# • one order containing several products
# • one order with no discount
# • one order with a discount
# • one express order
# • one order containing additional optional metadata
# Reuse the same functions wherever possible.
# Avoid creating separate functions for each order type.
# Final Challenge - Daily Order Report
# Create a report containing information about all orders processed during the day.
# The report should include at least:
# • number of orders
# • total revenue
# • average order value
# • largest order
# • smallest order
# Also include at least two additional statistics or pieces of information of your own choice.
# Create a flexible report function that can receive:
# • a report title
# • a variable number of report sections
# • optional metadata
# Metadata could include:
# • generated by
# • department
# • date
# • version
# • confidential status
# The function should return a structured report.
# Then create another function that converts the report into a readable multi-line string.
# Design Challenge
# Review your finished program and find at least three places where your choice of function parameters
# matters.
# For each one, explain in comments:
# • Why you used normal parameters, *args or **kwargs.
# • What alternative design you considered.
# • Why your final version is easier to use or understand.
# Also identify one place where using *args or **kwargs would actually make the function less clear and
# explain why.
# Requirements
# Your solution must demonstrate meaningful use of:
# • local and global scope
# • enclosing scope
# • *args
# • **kwargs
# • positional unpacking with *
# • dictionary unpacking with **
# • normal positional/named parameters
# • return values
# • functions calling other functions
# • collections from previous lessons
# Your program should:
# • use descriptive function and variable names
# • avoid unnecessary global state
# • avoid unnecessary repetition
# • separate calculations from presentation where reasonable
# • run without errors
# Restrictions
# Do not use:
# • classes
# • file handling
# • external libraries
# These concepts belong to later lessons.
# You are not required to use *args or **kwargs in every function. Part of the challenge is deciding when
# flexible parameters improve the design and when normal parameters are clearer.