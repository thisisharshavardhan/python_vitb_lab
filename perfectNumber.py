num = int(input("Enter a number: "))
sum = 0
for i in range(1,num):
    if(num%i == 0):
        sum = sum + i
if(num == sum):
    print("Perfect Number")
else:
    print("not a perfect Number")