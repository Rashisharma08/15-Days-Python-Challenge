# Write into file
file = open("student.txt", "w")
file.write("Name: Rashi")
file.close()

# Read file
file = open("student.txt", "r")
print(file.read())
file.close()
