a = int(input("Enter a side length: "))
b = int(input("Enter b side length: "))
c = int(input("Enter c side length: "))

if(((a+b)>c) and ((a+c)>b) and ((b+c)>a)):
    print("The triangle is valid")
else:
    print("The triangle is invalid")