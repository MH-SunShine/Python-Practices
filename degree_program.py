while True:
    degree = float(input("Enter your degree:"))
    if degree < 0 or degree > 20:
        print("NON VALID DEGREE...")
        break
    if degree >= 18:
        print("Excellent !")
    elif degree >= 15:
        print("Very good !")
    elif degree >= 12:
        print("Good !")
    elif degree >= 10:
        print("Acceptable")
    else:
        print("Failed :(")