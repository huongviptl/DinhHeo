while True:    
    a = int(input("Your weight?"))
    b = int(input("Your Height?"))
    c = float(a / ( (b/100)*(b/100) ))

    print("Your BMI:", c )

    if c < 16:
        print("Severely underweight")
    elif c < 18.5:
        print("Underweight")
    elif c < 25:
        print("Normal")
    elif c < 30:
        print("Overweight")
    else:
        print ("obese")
