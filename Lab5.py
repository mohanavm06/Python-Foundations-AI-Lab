# Mohana Muruganandham
# Lab 5
# Part A - Scope
def show_local():
    course_name = "Java Developer"  # local — shadows the global
    print("Inside function:", course_name)


show_local()
print("Outside function:", course_name)


# Create a function with a local counter and show that it does not remain available outside the function.
def count():
    counter = 0
    counter += 1
    print("Inside counter =", counter)


count()
# print("Outside counter =", counter)  # NameError!

# Create a function that attempts to modify a global numeric variable without global. Observe/describe the problem, then rewrite the design to return the new value instead.
total = 10


def add_five(total):
    return total + 5


total = add_five(total)


# Create a nested function and demonstrate a simple enclosing-scope lookup.
def outer():
    message = "Hello from outer"

    def inner():
        print(message)  # found in the outer scope

    inner()


outer()
# Create examples that avoid shadowing built-ins such as list, str, sum and max.
items = [3, 1, 2]  # inte "list"
name = "Mohana"  # inte "str"
total = 10  # inte "sum"
highest = 99  # inte "max"


# Part B - *args
# Write add_all(*numbers) returning the sum without sum().
def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(add_all(1, 2, 3, 4))


# Write average(*numbers). Decide what should happen when no numbers are supplied.
def average(*numbers):
    if not numbers:
        return 0
    return add_all(*numbers) / len(numbers)


print(average(2, 4, 6))
print(average())


# Write longest_word(*words) returning the longest word.
def longest_word(*words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# Write build_sentence(separator, *words) returning one joined string.
def build_sentence(separator, *words):
    return separator.join(words)


print(build_sentence(" ", "Hej", "there"))


# Write describe_scores(student_name, *scores) returning name, number of scores and average.
def describe_scores(student_name, *scores):
    return student_name, len(scores), average(*scores)


print(describe_scores("Sven", 8, 9, 10))


# Part C - Positional unpacking
# Create a list [10, 20, 30] and unpack it into a function expecting three positional parameters.
def add_three(a, b, c):
    return a + b + c


numbers = [10, 20, 30]
print(add_three(*numbers))


# Create a tuple containing first_name, last_name, city and call a function using *tuple.
def greet(first_name, last_name, city):
    return f"Hello {first_name} {last_name} from {city}!"


person = ("Mohana", "Muruganandham", "Stockholm")
print(greet(*person))

# Use starred assignment: first, *middle, last = values. Test with several list lengths.
for values in [
    [1, 2, 3, 4, 5],
    [10, 20],
    [7, 8, 9],
]:
    first, *middle, last = values
    print(f"values={values} -> first={first}, middle={middle}, last={last}")

# Explain in comments the difference between * in a function definition and * in a function call.

# In a definition, *name packs variables
# In a call, *iterable unpacks varables


# Part D - **kwargs
# Write show_profile(**info) and iterate over all key/value pairs.
def show_profile(**info):
    for item in info.items():
        print(item)


# Write create_user(username, **details) returning one dictionary containing username plus all supplied details.


def create_user(username, **details):
    return {"user": username, **details}


# Write build_product(name, price, **metadata) returning a dictionary.
def build_product(name, price, **metadata):
    return {"name": name, "price": price, **metadata}


product = build_product(
    "Keyboard",
    899,
    brand="Keychron",
    layout="ISO",
    wireless=True,
)
print(product)


# Write a function that accepts **settings and returns only settings whose value is not None.
def read_settings(**settings):
    active_settings = {}
    for key, value in settings.items():
        if value is not None:
            active_settings[key] = value
    return active_settings


# Call a normal named-parameter function using **dictionary unpacking. Ensure dictionary keys match parameter names.


def greet(name, city, language):
    return f"Hello {name} from {city}, you speak {language}!"


info = {"name": "Mohana", "city": "Swiss", "language": "German"}
print(greet(**info))

# Part E - Combining parameters
# Create log_event(event_type, *messages, **metadata) returning a structured dictionary.


def log_event(event_type, *messages, **metadata):
    return {
        "event_type": event_type,
        "messages": messages,
        "metadata": metadata,
    }


# Create calculate_order(customer, *prices, **options). Support an optional discount and shipping fee in options.
def calculate_order(customer, *prices, **options):
    order_sum = sum(prices)
    discount = options.get("discount", 0) * order_sum
    shipping = options.get("shipping", 0)

    return order_sum + shipping - discount


# Create a function where explicit named parameters would be clearer than **kwargs. Write both versions and compare readability in comments.
def create_user_kwargs(username, **options):
    email = options.get("email")
    age = options.get("age")
    is_admin = options.get("is_admin", False)
    newsletter = options.get("newsletter", True)
    return {
        "username": username,
        "email": email,
        "age": age,
        "is_admin": is_admin,
        "newsletter": newsletter,
    }


def create_user(username, email=None, age=None, is_admin=False, newsletter=True):
    return {
        "username": username,
        "email": email,
        "age": age,
        "is_admin": is_admin,
        "newsletter": newsletter,
    }


# Use **kwargs when the set of keys is genuinely open-ended or you're forwarding
# them to another function


# Create at least three calls to the same flexible function with substantially different numbers of arguments.
def greet(*names, **opts):
    greeting = opts.get("greeting", "Hej")
    return f"{greeting} {', '.join(names)}!"


print(greet("Mohana"))
print(greet("Mohana", "Sam", "Erik"))
print(greet("Mohana", "Sam", "Erik", "Maja", "Sai", greeting="Hallå"))


# Part F - Applied challenge: Report builder
# Build a flexible report system without files. create_report(title, *sections, **metadata) should return a dictionary.
# Each section can be a string or a small dictionary; choose and document your design.
# Metadata may include author, department, version, confidential and date.
def create_report(title, *sections, **metadata) -> dict:
    return {
        "title": title,
        "sections": list(sections),
        "metadata": metadata,
    }


# Write summarize_report(report) that returns a readable multi-line string.
def summarize_report(report) -> str:
    lines = [f"Title: {report['title']}"]
    for key, value in report["metadata"].items():
        lines.append(f"{key}: {value}")
    lines.append(f"Sections: {len(report['sections'])}")
    return "\n".join(lines)


# Write count_words(*sections) that counts words across all supplied textual sections.
def count_words(*sections) -> int:
    return sum(len(s.split()) for s in sections)


meta_q3 = {"author": "Mohana", "department": "Planering", "version": "1.0"}
meta_q4 = {
    "author": "Anna",
    "department": "Maths",
    "version": "2.1",
    "confidential": True,
}

# Use dictionary unpacking to create at least two reports from predefined metadata dictionaries.

report1 = create_report(
    "Q3", "Försäljningen ökade.", "Kostnaderna minskade.", **meta_q3
)
report2 = create_report("Q4", "Nya marknader.", **meta_q4)

# Demonstrate at least one case where your function deliberately ignores or handles a missing optional metadata field.
print(summarize_report(report1))
print()
print(summarize_report(report2))
print("Ord i Q3:", count_words(*report1["sections"]))

# Part G - Stretch challenges
# Write merge_settings(defaults, **overrides) returning a new dictionary without modifying defaults.
# Write call_summary(function_name, *args, **kwargs) returning a string describing what would be called.
# Write a flexible statistics function that returns count, total, average, min and max for *numbers. Implement the calculations manually where reasonable.
# Create five "predict the output" scope questions and verify your predictions.
