<<<<<<< HEAD
# another attempt to create a basic calculator

number1 = int(input("enter the first value:"))
number2 = int(input("enter the second value:"))
choice = int(input("\n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n 5.modulo \n 6.power \nenter your choice:"))

if choice == 1:
    print(f"your choice = {choice} -> {number1} + {number2} = {number1 + number2}")
elif choice == 2:
    print(f"your choice = {choice} -> {number1} - {number2} = {number1 - number2}")
elif choice == 3:
    print(f"your choice = {choice} -> {number1} * {number2} = {number1 * number2}")
elif choice == 4:
    print(f"your choice = {choice} -> {number1} / {number2} = {round(number1 / number2, 2)}")
elif choice == 5:
    print(f"your choice = {choice} -> {number1} % {number2} = {number1 % number2}")
elif choice == 6:
    print(f"your choice = {choice} -> {number1} ** {number2} = {number1 ** number2}")
else:
    print(f"{choice} not a valid operator. try again :)")
=======
# another attempt for a basic calculator
# operation is made according to the user choice

number1 = int(input("enter the first value:"))
number2 = int(input("enter the second value:"))
choice = int(input("\n 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n 5.modulo \n 6.power \nenter your choice:"))

if choice == 1:
    print(f"your choice = {choice} -> {number1} + {number2} = {number1 + number2}")
elif choice == 2:
    print(f"your choice = {choice} -> {number1} - {number2} = {number1 - number2}")
elif choice == 3:
    print(f"your choice = {choice} -> {number1} * {number2} = {number1 * number2}")
elif choice == 4:
    print(f"your choice = {choice} -> {number1} / {number2} = {round(number1 / number2, 2)}")
elif choice == 5:
    print(f"your choice = {choice} -> {number1} % {number2} = {number1 % number2}")
elif choice == 6:
    print(f"your choice = {choice} -> {number1} ** {number2} = {number1 ** number2}")
else:
    print(f"{choice} not a valid operator. try again :)")
>>>>>>> f2ed750d7a17335c9022ac89adae01136d360ce3
