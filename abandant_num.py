num=int(input("enter the number:"))

sum=1  #1 is can divide any number

for i in range(2,num):
    if(num%i==0):
        sum+=i
if(sum>num):
    print("its a abundant number")       
else:
    print("its not abundant number")

