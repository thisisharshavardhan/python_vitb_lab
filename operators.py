a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
# arithmetic operators
print("arithmetic operators")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

# relational opterators
print("relational operators")
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

# assignment operators
print("Assignment operators")
c  = a
c += a
c -= a
c /= a
c *= a

# logical operators
print("logical operators")
print(True and True)
print(True or false)
print(not True)

# bitwise operators
print("bitwise operators")
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<b)
print(a>>b)

# membership operators
print("membership operators")
list1 = [1,2,3,4]
print(2 in list1)
print(3 not in list1)

# identity operators
print("identity operators")
list2 = list1
print(list1 is list2)
print(list1 is not list2)
