n = int(input("Enter n value: "))
original=n
sum = 0
while(n>0):
    rem = n%10
    sum = sum + rem**3
    n= n//10
if(sum == original):
    print("The number you entered is an armstrong number")
else:
    print("THe number you entered is not an armstrong number")