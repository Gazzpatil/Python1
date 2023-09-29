# perfect number



gazz=int(input("enter the number:"))

assmita=0

for i in range(1,gazz):
    if gazz%i==0:
        assmita+=i
if(assmita==gazz):
    print("it is a perfect number") 
else:
    print("it is not a perfect number")           