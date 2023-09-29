num=int(input("enter the number:"))

a=0
for i in range(1,num):
    if(num%i==0):
        a+=i
if (num==a):
    print("its a perfect number ")        
else:
    print("its not a perfect number")    
