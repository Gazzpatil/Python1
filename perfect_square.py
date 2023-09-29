# to find the perfect square of a number
#  4=2*2,  9=3*3 , 16=4*4
num = int(input("enter the number"))
gazz=0
for i in range(1,num):
    if i*i==num:
        gazz=1
        break

if gazz==1:
    print("it is a perfect square")
else:
    print("it is not")    

