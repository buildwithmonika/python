name = input("Enter your name: ") #by default input is string
print(name)

#coverting data to other input types
age = int(input("Enter your age: ")) #converting string to integer
print(type(age))

height = float(input("Enter your height: ")) #converting string to float
print(type(height))

# taking multiple inputs
a, b = input("Enter two number separated by space: ").split() #by default input is string
print("a:", a)
print("b:", b)

# taking multiple inputs
numbers = input("Enter list separated by space: ").split()
print(numbers)

#handling extra spaces
branch = input("Enter your branch: ").strip() #removing extra spaces
print("Branch:", branch)



