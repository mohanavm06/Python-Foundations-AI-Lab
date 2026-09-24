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
classes implement the exact same method signature (`send()`). 

As long as every object in the list responds to the `.send()` method call, the loop 
can treat them uniformly without needing to check their specific type or class.
"""
# Part B - Polymorphism with inheritance
