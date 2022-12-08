num1 = int(input("type a number: "))
num2 = int(input("type a number: "))

if num1%2==0 and num2%2==0:
    print("")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} pair")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} pair")
else:
    print("both are odd")