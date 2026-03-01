# Day 2 - Result and Grading System

m = int(input("Enter Maths marks: "))
s = int(input("Enter Science marks: "))
e = int(input("Enter English marks: "))

total = m + s + e
print("Total:", total)

percentage = (total / 300) * 100
print("Percentage:", percentage)

if m >= 33 and s >= 33 and e >= 33:

    if percentage >= 75:
        print("Result: Pass")
        print("Grade: A")

    elif percentage >= 60:
        print("Result: Pass")
        print("Grade: B")

    elif percentage >= 40:
        print("Result: Pass")
        print("Grade: C")

    else:
        print("Result: Fail")

else:
    print("Result: Fail")
