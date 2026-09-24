# Python Fundamentals – Lexicon Labs

## Overview

This repository contains my Python Fundamentals lab exercises completed as part of the **Python and AI training at Lexicon**.

The labs build progressively from basic Python syntax and data types to functions, collections, object-oriented programming, inheritance, polymorphism, composition, and Pythonic data processing.

The purpose of this repository is to document my learning journey, strengthen my programming fundamentals, and demonstrate how I apply Python concepts through practical exercises and small challenges.

---

# Learning Progression

## Lab 1 – Python Basics and Strings

Lab 1 introduced the foundations of Python programming.

### Topics Covered

* Variables
* Data types
* Type conversion
* Arithmetic operators
* User input
* Calculations
* Strings
* String indexing
* String slicing
* String methods
* f-strings
* String immutability

### Exercises

Examples included:

* Printing personal and course information
* Working with integers, floats, strings and booleans
* Performing arithmetic calculations
* Converting between data types
* Calculating age from year of birth
* Calculating discounts
* Celsius to Fahrenheit conversion
* Calculating room area and perimeter
* Working with names and formatted strings
* Creating usernames
* Extracting email components
* Replacing text
* Practicing string slicing

### Applied Challenge

Built a console-based registration summary that collects:

* First name
* Last name
* City
* Year of birth
* Favourite programming language

The program also creates a generated user ID and prints derived information using only the concepts introduced in the lesson.

---

## Lab 2 – Collections in Python

Lab 2 introduced Python collections and how different data structures are used for different situations.

### Topics Covered

* Lists
* Tuples
* Sets
* Dictionaries
* Nested collections
* Indexing and slicing
* List methods
* Sorting
* Copying lists
* Tuple unpacking
* Set operations
* Dictionary methods

### Exercises

Examples included:

* Creating and modifying lists
* Sorting lists
* Understanding `.sort()` and `sorted()`
* Understanding reference versus copy
* Working with tuples and unpacking
* Removing duplicates using sets
* Finding common and unique values
* Working with dictionaries
* Updating dictionary values
* Using `.get()`
* Working with nested dictionaries and lists

### Applied Challenge

Created a personal media catalogue containing multiple items such as movies, games, or books.

The challenge involved:

* Lists of dictionaries
* Sets for unique categories
* Tuples for immutable identifiers
* Nested indexing
* Updating stored information
* Printing structured summaries

---

## Lab 3 – Conditions and Loops

Lab 3 focused on decision-making and repetitive program flow.

### Topics Covered

* `if`
* `elif`
* `else`
* Comparison operators
* Boolean logic
* Truthy and falsy values
* Membership testing
* `for` loops
* `while` loops
* `range()`
* `enumerate()`
* Nested loops
* `break`
* `continue`

### Exercises

Examples included:

* Positive, negative, or zero classification
* Age-group classification
* Login validation
* Grade calculation
* Shipping rules
* Membership checking
* Iterating through lists
* Counting values
* Finding maximum values manually
* Multiplication tables
* Countdown programs
* Password loops
* Repeated menus
* Running totals
* Guessing loops

### Applied Challenge

Built a console-based study tracker.

The program works with study sessions and includes:

* Total study time
* Study time per subject
* Longest study session
* Filtering sessions
* Repeated menu interaction
* `break` and `continue`

---

## Lab 4 – Functions

Lab 4 introduced reusable functions and structured program design.

### Topics Covered

* Function definitions
* Parameters
* Arguments
* Return values
* Default parameters
* Keyword arguments
* Functions with collections
* Decomposition
* Type hints
* Docstrings

### Exercises

Examples included:

* Greeting functions
* Arithmetic functions
* Area calculation
* Checking even numbers
* Finding larger values
* PASS/FAIL classification
* Formatting names
* Discount calculations
* Working with lists and dictionaries inside functions

### Decomposition

Larger problems were divided into smaller reusable functions.

Examples included:

* Temperature report
* Order calculation
* Refactoring repeated code
* Creating a clear main program flow

### Stretch Challenges

Included:

* Minimum and maximum without built-in functions
* Palindrome checking
* Character frequency counting
* Positive, negative and zero counting
* Adding type hints and docstrings

---

## Lab 5 – Scope, `*args` and `**kwargs`

Lab 5 expanded function knowledge by introducing scope and flexible arguments.

### Topics Covered

* Global scope
* Local scope
* Enclosing scope
* Variable shadowing
* `*args`
* `**kwargs`
* Positional unpacking
* Dictionary unpacking
* Flexible function signatures

### Exercises

Examples included:

* Comparing local and global variables
* Working with nested functions
* Avoiding built-in name shadowing
* Adding multiple numbers with `*args`
* Calculating averages
* Finding longest words
* Building sentences
* Creating flexible user/profile functions
* Passing dictionaries with `**`

### Applied Challenge

Built a flexible report system using:

```python
create_report(title, *sections, **metadata)
```

The report system supports information such as:

* Author
* Department
* Version
* Confidential status
* Date

Additional functionality included summarizing reports and counting words.

---

## Lab 6 – Pythonic Data Processing

Lab 6 focused on writing cleaner and more concise Python.

### Topics Covered

* List comprehensions
* Dictionary comprehensions
* Set comprehensions
* Conditional comprehensions
* `enumerate()`
* `zip()`
* Tuple unpacking
* `sorted()`
* Lambda functions
* Data cleaning
* Data transformation

### Exercises

Examples included:

* Creating squares
* Filtering even numbers
* Cleaning names
* PASS/FAIL transformations
* Building dictionaries from values
* Removing duplicates
* Numbering items using `enumerate()`
* Combining related lists using `zip()`
* Sorting by custom rules
* Sorting with lambda functions

### Applied Challenge – Data Cleanup

Created a dataset containing messy product information and cleaned it.

Tasks included:

* Normalizing product names
* Normalizing categories
* Filtering in-stock products
* Finding unique categories
* Calculating inventory value
* Sorting inventory from highest to lowest
* Producing a ranked report
* Combining related values using `zip()`

This lab helped connect Python fundamentals with practical data-cleaning tasks.

---

## Lab 7 – Object-Oriented Programming Fundamentals

Lab 7 introduced classes and objects.

### Topics Covered

* Classes
* Objects
* `__init__`
* Instance attributes
* Class attributes
* Methods
* Object state
* Collections of objects
* Objects inside objects
* Validation with `ValueError`

### Exercises

Examples included:

* `Book`
* `Laptop`
* `BankAccount`
* `Task`
* `Product`
* `Student`
* `Teacher`
* `Course`

The exercises demonstrated how each object can maintain its own state and behaviour.

### Applied Challenge – Course Manager

Built a small course-management system using:

* `Student`
* `Teacher`
* `Course`

The system includes:

* Student scores
* PASS/FAIL status
* Teacher information
* Adding students
* Counting students
* Filtering passed students
* Input validation
* Course summary generation

---

## Lab 8 – Inheritance and Method Overriding

Lab 8 expanded object-oriented programming with inheritance.

### Topics Covered

* Mutable default arguments
* Safe defaults using `None`
* Dictionary versus class
* Inheritance
* `super()`
* Shared initialization
* Subclass-specific behaviour
* Method overriding
* Validation
* IS-A relationships

### Exercises

Examples included:

* `Team`
* `Movie`
* `Account`
* `SavingsAccount`
* `Employee`
* `Developer`
* `Device`
* `Laptop`
* `Notification`
* `EmailNotification`
* `SMSNotification`
* `Report`
* `SalesReport`

### Applied Challenge – User Accounts

Built a user-account system with:

* `User`
* `AdminUser`
* `PremiumUser`

The system demonstrates:

* Inherited methods
* Subclass-specific methods
* Overridden methods
* `super()`
* Validation
* IS-A relationships

----------------------------------------------
**TechnologiesUsed** 
Python 3
VS Code
Git
GitHub
Terminal
macOS

----------------------------------------------

# Author

**Mohana Muruganandham**

Python & AI Training – Lexicon
