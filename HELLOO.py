first = eval(input("enter the first number: "))
operator = input("enter operator (+,-,*,/,%) ")
second = eval(input("enter second number: "))
if operator == "+":
    print( first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first  * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("error 404 ")