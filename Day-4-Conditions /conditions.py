# 1. Age Check Program
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")


# 2. Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 3. Grade Program
marks = int(input("Enter Marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# 4. Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)


# 5. Divisible by 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
