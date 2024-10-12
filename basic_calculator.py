number1 = int(input("enter the first value:"))
number2 = int(input("enter the second value:"))
operator = input("enter the operator  (+ - * / % **):\t")

if operator == '+':
    result = number1 + number2
    print(result)
elif operator == '-':
    result = number1 - number2
    print(result)
elif operator == '*':
    result = number1 * number2
    print(result)
elif operator == '/':
    result = number1 / number2
    print(result)
elif operator == '%':
    result = number1 % number2
    print(result)
elif operator == '**':
    result = number1 ** number2
    print(result)
else:
    print(f"{operator} not a valid operator. try again :)")