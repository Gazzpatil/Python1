# by using math module to find factorial of a number
'''import math
num=23
print(math.factorial(num))'''

# by using iteration method

'''num=5
fact=1
for i in range(2,num+1):
    fact=fact*i
print(fact)'''

#by recursion method

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)    
print(factorial(5))