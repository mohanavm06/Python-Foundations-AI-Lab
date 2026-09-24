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
# Part A - Polymorphism
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
# Part B - Polymorphism with inheritance
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

        

