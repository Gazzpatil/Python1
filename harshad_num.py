n =int(input("enter the number:"))
g=n
sum=0
while(n>0):
    sum+=n%10
    n=n//10
if(g%sum==0):
    print("Harshad number")
else:
    print("Not harshad number")
         