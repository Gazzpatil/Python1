#factorial using iteration method

gazz=int(input("enter the number to find the factorial of number"))

fact=1
for i in range(2,gazz+1):
    fact=fact*i
print(fact)