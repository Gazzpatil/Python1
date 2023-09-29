g = int(input("enter the number to know weather it is armstrong number or not:"))
gazz=g
sum=0

while g>0:
    sum= sum+ g%10*g%10*g%10
    g=g//10

if gazz==sum:
    print("it is a armstrong number")  
else:
    print("it is not armstrong number")      