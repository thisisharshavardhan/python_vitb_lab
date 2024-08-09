a = 0
b = 1
next = b
count = 1

while count <= 100:
    print(next)
    count +=1
    a= b
    b = next
    next = a+b