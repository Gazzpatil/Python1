gazz=int(input("Enter the number:"))
count=0
for i in range(1,gazz):
    if (gazz%i):
        count=1
        break
if count==1:
    print("its a prime number:")
else:
    print("its not prime number")