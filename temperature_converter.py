unit = input("is this temperature in Celsius (C) or in Fahrenheit (F) ?\n")
temperature = float(input("enter the temperature value:"))

if unit == 'C':
    result = round((temperature * 9)/5 + 32, 1)
    print(f"{temperature} in Fahrenheit = {result}°F")
elif unit == 'F':
    result = round((temperature - 32) * 5/9, 1)
    print(f"{temperature} in Celsius = {result}°C")
else: 
    print(f"{unit} not a valid unit. try again :)")