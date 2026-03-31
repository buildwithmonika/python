print("Hello, world!!!!") # basic print function

# printing multiple values
name = "Monika"
age = 25
print(name, age)

# printing with custom separator
print(name, age, sep = "-")

# printing with end parameter
print(name, age, sep="-", end="....")
print("A", "B", "C", sep=" | ", end="....\n") # adding new line at the end

# string concatenation using print
print("Hello, " + name + "!!")
print("Hello, ", name)

# f-strings for formatted printing
print(f"Hello, {name}! You are {age} years old.")

# aligning text using f-strings
print(f"{'Name':<10}{'Age':>5}")
print("-" * 15)
print(f"{'Monika':<10}{25:>5}")
print(f"{'Alice':<10}{30:>5}")

print(f"{'First Name':<15}{'Last Name':^10}{'Age':>2}") # < left align with 15 characters, ^ center align, > right align
print("-" * 27)
print(f"{'Mona':<15}{'Singh':^10}{'25':>2}")

# formatting numbers
pi = 3.14159
print(f"Value of pi: {pi:.2f}") 

# printing emojis using Unicode
smile = "\U0001F600"
print(f"Hello, {smile}")
