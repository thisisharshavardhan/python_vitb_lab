n = int(input("Enter n value: "))
original = n
reverse = 0
while n>0:
    rem = n%10
    reverse = reverse * 10 + rem
    n = n//10
if(reverse == original):
    print("Number is palindrom")
else:
    print("Number is not a palindrom")