# 5! = 1 X 2 X 3 X 4 X 5   # factorial of 5

# print factorial of n

n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")