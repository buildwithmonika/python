n, m = 4, 10
for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 or i == n or j == 1 or j == m:
            print("*", end="")
        else:
            print(" ", end="")
    print()

        

# n = 4
# counter = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(counter, end=" ")
#         counter += 1
#     print()

    

# n, m = 4, 10
# for i in range(1, n+1):
#     for i in range(1, m+1):
#         print("*", end="")
#     print()



