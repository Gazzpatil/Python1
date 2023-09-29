
# palindrome of a number by string
'''
gazz = input("enter the number")
revrse=gazz[::-1]

if gazz==revrse:
    print("it is palindrome")
else:
    print("it is not palindrome")'''   
    


#finding palindrome by integer number

number = int(input("enter the number"))
gazz =number
assmita=0
while number>0:
    dig=number%10
    assmita=assmita*10+dig
    number=number//10
if gazz==assmita:
    print("the number is palindrome")    
else:
    print("the number is not palindrome")    
