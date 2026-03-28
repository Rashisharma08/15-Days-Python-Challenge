# Function without parameter
def greet():
    print("Welcome to Python")

greet()


# Function with parameter
def greet_user(name):
    print(f"Hello {name}")

greet_user("Rashi")


# Function with return value
def add(a, b):
    return a + b

result = add(5, 10)
print("Sum =", result)
