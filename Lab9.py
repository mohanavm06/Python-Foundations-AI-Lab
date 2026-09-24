# Mohana Muruganandham
# Lesson Nine
# Python AI 
# Lab 9 
# Email Notification ──> send()
# SMSNotification   ──> send()
# PushNotification  ──> send()
#                          ↑
#                   same method name
#                   different behaviour
# ==========================================
# Part A - Polymorphism
# ==========================================
# 1. Create three classes
class EmailNotification:
    # 2. Give all three classes a method called send() with a different return message
    def send(self):
        return "Sending Email: Check your inbox!"
class SMSNotification:
    def send(self):
        return "Sending SMS: Check your text messages!"
class PushNotification:
    def send(self):
        return "Sending Push Notification: Check your phone alerts!"

# 3. Create one object from each class and store them in the same list
notifications = [
EmailNotification(),
SMSNotification(),
PushNotification()
]
# 4. Loop through the list and call send() on every object
for notification in notifications:
    print(notification.send())
    # 5. Explanation of why the loop does not need to know the exact class:
"""
EXPLANATION:
This loop relies on Polymorphism (specifically dynamic duck typing in Python). 
The loop does not need to know the exact class of each object because all three 
classes implement the same method signature (`send()`). 

As long as every object in the list responds to the `.send()` method call, the loop 
can treat them uniformly without needing to check their specific type or class.
"""
# ==========================================
# Part B - Polymorphism with inheritance
# ==========================================
# 1. Base class Document with title attribute and describe() method
class Document:
    def __init__(self,title):
        self.title = title
    def describe(self):
        return f"Document: {self.title}"
# 2. Subclasses inheriting from Document
class PDFDoucment(Document):
# 3. Override describe() method
    def describe(self):
        return f"PDF Document: '{self.title}' (Portable Document Format, read-only layout)"
class TextDocument(Document):
    def describe(self):
        return f"TextDocument: '{self.title}'(Plain Text formate, easily editable)"
# 4. Create several PDFDocument and TextDocument objects in one list
documents = [
    PDFDocument("Mohana.pdf"),
    TextDocument("Notes.txt"),
    PDFDocument("User_Manual.pdf"),
    TextDocument("TodoList.txt")
]

# 5. Loop through the list and print each title and describe() result. 
for doc in documents:
    print(f"Title: '{doc.title}' | Description: {doc.describe()}")
    
# ==========================================
# Part C - Duck Typing
# ==========================================

# 1. Create two unrelated classes (no shared base class or inheritance)
class Printer:
# 2. Add display_status() method
    def display_status(self):
        return "Status: Online - Ink level 85%, Paper tray loaded."
class Screen:
    def display_status(self):
        return "Printer Status: Active - Resolution 1920x1080, Brightness 75%."
devices =[Printer(),Screen()]

print("--- Part C: Duck Typing ---")
for device in devices:
    print(device.display_status())

# ==========================================
# Part D - isinstance()
# ==========================================
class User:
    pass
class AdminUser(User):
    pass
admin = AdminUser()
print("--- Part D: isinstance() ---")
is_admin = isinstance(admin,AdminUser)
is_user =  isinstance(admin, User)
is_string = isinstance(admin,str)
print(f"Is instance of AdminUser? {is_admin}")
print(f"Is instance of admin? {is_user}")
print(f"Is instance of str? {is_string}")       
# ==========================================
# Part E -  __str__
# ==========================================
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
# 3. Add __str__ for a human-readable description
    def __str__(self):
        return f"Product: {self.name} | Price: ${self.price:.2f}"
# 2. Observe printing before __str__ is defined:
# Without __str__, printing an object outputs its memory address:
# <__main__.Product object at 0x7f9a1020d9d0>
# 4. Create at least three Product objects and print them
p1=Product("Laptop",30000.00)
p2=Product("Wireless Mouse",13000.25)
p3=Product("Mechanical Keyboard",750.75)

print("---Part E:---- __str___")
print(p1)
print(p2)
print(p3)
# 5. Use str() on one Product object, store it in a variable and print its type    
product_string = str(p1)
print(f"String output:{product_string}")
print(f"Type of result: {type(product_string)}")
# ==========================================
# Part F - __str__ with inheritance
# ==========================================
# 1. Base class Account with owner and balance
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
# 2. Add __str__ to Account
    def __str__(self):
        return f"Account Owner: {self.owner} | Balance: ${self.balance:.2f}"
# 3. Subclass SavingsAccount inheriting from Account
class SavingsAccount:
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balace)
        self.interest_rate=interest_rate
# 4. Override __str__ to include the interest rate
    def __str__(self):
        # Optionally use super().__str__() to avoid repeating parent string formatting
        return f"{super().__str__} | Interestrate:{self.interest_rate}%"
        # 5. Create and print both an Account and a SavingsAccount object
print("\n--- Part F: __str__ with inheritance ---")
base_account = Account("Alice Smith", 1500.00)
savings_account = SavingsAccount("Bob Jones", 5000.00, 3.5)

print(base_account)
print(savings_account)
