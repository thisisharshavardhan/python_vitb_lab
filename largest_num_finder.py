a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))

if a>b and a>c:
    print(a," is greatest")
elif(b>a and b>c):
    print(b," is greatest")
else:
    print(c," is greatest")