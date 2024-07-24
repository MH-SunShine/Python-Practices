# this program handles 2 types of exception
while True:
    try:
        n1 = int(input("enter first number:"))
        n2 = int(input("enter second number:"))
        print(n1, "/", n2, "=", n1/n2)
        break
    except ValueError as value_exception:
        print("invalid error ! enter a number")
    except ZeroDivisionError as zero_exception:
        print("don't divide by zero !")