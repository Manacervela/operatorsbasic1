'''
A, a – addition
S, s – subtraction
m, p, M, m – Multiplication
D, d - Division'''


num1 = float(input("Type a number: "))
num2 = float(input("Type a number: "))

operator = input("Type the operation: ").upper()

if operator=='A':
    suma = num1+num2
    print(f"\n + is: {addition}")
elif operator == 'S':
    resta = num1-num2
    print(f"\n - is: {subtraction}")
elif operator=='M' or operator=='P':
    mult = num1*num2
    print(f"\n * is: {mult:.2f}")
elif operator=='D':
    div = num1/num2
    print(f"\n / is : {div:.2f}")
else:
    print("\nError, Type the operator again")