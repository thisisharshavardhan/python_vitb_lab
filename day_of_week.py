day = int(input("Enter a day between 1-7: "))
list = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
if(day>0 and day<8):
    print(list[day-1])
else:
    print("invalid choice")