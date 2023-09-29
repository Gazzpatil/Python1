num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

if num1>num2:
    min=num2
else:
    min=num1


for i in range(1,min+1):
    if num1%i==0  and num2%i==0:
        hcf=i
print("the hcf/gcd of the numbers is:",hcf)
