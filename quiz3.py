#python example project_3
#UNIT_CONVERTER

    #ask the user to which unit of measurement that they want to convert. 
while True:
    print("To which unit of measurement you want to convert?")
    print("1, km to miles")
    print("2, km to cm")
    print('3, km to m')
    unit = int(input("Choose from the options above: enter 1, 2, or 3:--->"))
        #ask the user to put the value of their measurement
    value = float(input('enter your mesurement here:- '))
        #give the converted unit to the user
    if unit == 1:
        print("converted mile is :-", value * 0.62)
    elif unit == 2:
        print("converted centimeter is :-", value * 10000)
    elif unit == 3:
        print("converted meter is :-", value * 1000)
    else:
        print("PLEASE CHOOSE 1, 2, OR 3.")
        break