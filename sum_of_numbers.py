n = int(input("Enter n value: "))
sum = 0
for i in range(1,n+1):
    sum+=i
print("sum of numbers using for: ",sum)

sum = 0
i = 0
while(i<=n):
    sum+=i
    i+=1
print("sum of numbers using while: ",sum)