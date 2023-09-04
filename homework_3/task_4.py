user = input("Enter text: ")
var = user.split()
print(var)
print(user[-3:])


if len(user) < 3:
   print("The number of elements is less than 3")
else:
   print("Correct elements")

