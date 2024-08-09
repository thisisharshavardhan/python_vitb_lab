for i in range(1,6):
    print("* "*i)

for i in range(1,6):
    for k in range(1,i+1):
        print(k,end=" ")
    print()

l = ["A ","B ","C ","D ","E ","F ","G ","H ","I ","J ","K ","L ","M ","N ","O "]
for i in range(1,6):
    print(l[i-1]*i)
count = 0
for i in range(1,6):
    for k in range(1,i+1):
        print(l[count],end="")
        count+=1
    print("")