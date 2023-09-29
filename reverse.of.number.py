gazz=int(input("enter the number:"))

reverse=0
if gazz==0 or gazz<0:
    print("not a valid number")
else:
        while gazz>0:
    
            reverse= (reverse*10) + gazz%10
            gazz= gazz//10


print(reverse)    