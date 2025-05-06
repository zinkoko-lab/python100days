# def greet():
#     print("Hello!")
#     print("How do you do?")
#     print("Isn't the weather nice?")
#
# greet()

# Function that allows for inputs

# def greet_with_name(name):
#     print(f"Hello, {name}!")
#     print(f"How do you do?, {name}.")
#
# greet_with_name("JIN")

# Functions with more than 1 inputs

def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"What is it like in {location}?")

# Positional arguments
# greet_with("JIN", "Nowhere")
# greet_with("Nowhere", "JIN")

# Keyword arguments
greet_with(location="Nowhere", name="JIN")