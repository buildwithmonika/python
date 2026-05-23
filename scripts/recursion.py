n = int(input("Enter number to get factorial:"))

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(n))


# n = int(input("Enter any digit: "))
# def n_func(n):
#     if n == 0:
#         return 0
    
   
#     n_func(n-1)
#     print(n, end="")
    

# n_func(n)
