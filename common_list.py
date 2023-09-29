#5. Compare two lists in python and return matches in python
'''list1=[10,20,49,1,2,3,4,5,6,8,39]
list2=[34,55,6,4,51,10,20,506,6,]
print(set(list1) & set(list2))'''

#How to Remove Duplicates From a Python List

'''list=[10,434,56,10,10,3,535,34,34,3,4,3,4]
print(set(list))'''

#how to reverse a list in python
#using slicing
'''list=[10,29,'gazz',80,1,2,5,'ash']
print(list[::-1])'''

#using reverse function
'''list=[10,40,32,5,9,8,10,'gazz','ash']
list.reverse()
print(list)'''

#9. How to make a string palindrome in Python

'''str1=input("enter the name:")

if str1.lower()==str1[::-1].lower():
    print("Its a palindrome!!")
else:
    print("Its not a palindrome!")'''
#by using user defined function
'''def ispalindrome(s):
    if s.lower()==s[::-1].lower():
        print("Its palindrome:")
    else:
        print("its not palindrome:")
s=input("enter the string to check palindrome:")
gazz=ispalindrome(s)'''

#10. Find the Second Largest Number in a list in Python

'''list=[10,47,60,48,100,454,1000]
list.sort()
print(list)
print(list[-2])'''

#Method 2: Using Python’s built-in method set & remove

list=[10,20,30,10,50,100,500]
new_list=set(list)
new_list.remove(max(new_list))
print(f"the second largest number from the list is {max(new_list)}")