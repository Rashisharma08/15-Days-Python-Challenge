# Day 3 Python Practice
# Rashi Sharma

# Reverse String
text = "python"
print("Reverse:", text[::-1])

# Even Odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Largest number in list
numbers = [4,7,2,9,5]
print("Largest:", max(numbers))

# Factorial
num = 5
fact = 1

for i in range(1, num+1):
    fact = fact * i

print("Factorial:", fact)
