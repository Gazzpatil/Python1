#if we square a number and the product of that square ends  with the same number as the number which we did square is known as automorphic number



gazz=int(input("enter the number:"))

gazz1=str(gazz)
square=gazz*gazz
square1=str(square)

if square1.endswith(gazz1):
    print("auto morphic number:")

else:
    print("its not automorphic number")
    