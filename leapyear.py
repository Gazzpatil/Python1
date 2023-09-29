year = int(input("enter the number:"))


if year%400==0 or (year%4==0 and year%100  !=0):
    print("it is aleap year")
else:
    print("not a leap year")    