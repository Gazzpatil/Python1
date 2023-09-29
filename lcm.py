num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
maxnumb = max(num1,num2)
while(True):
    if(maxnumb%num1==0  and  maxnumb%num2==0):
        break
    maxnumb=maxnumb+1

print(f"LCM of {num1} and {num2} is {maxnumb}")