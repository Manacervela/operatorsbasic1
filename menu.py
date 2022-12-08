left = 15000

option = int(input("Type one of the option above: "))

if option==1:
    extra = float(input("How much money do you want to put in -> "))
    left += extra
    print(f"Money in account: {left}")
elif option==2:
    withdraw = float(input("How much money do you want to withdraw -> "))
    if withdraw>left:
        print("not enough to withdraw that amount")
    else:
        left -= withdraw
        print(f"balance: {left}")
elif option==3:
    print(f"balance: {left}")
elif option==4:
    print("Thank you")
else:
    print("Error, type an option again please")
