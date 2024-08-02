n = int(input("Enter n value: "))
count = 0
i = 1
while (i<=n):
    if n%i==0:
        count+=1
    i+=1
if (count == 2):
    print("Prime number")
else:
    print("Not a prime number")