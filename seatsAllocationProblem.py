# initialize all seats to zero or empty. we need next 3 lines of code to empty the seats. We can comment after once use.
# Row1=['0']*8
# Row2=['0']*8
# Row3=['0']*8

userInput= int(input("Enter the number of seats requested: ")) # take the input from user

#conditions for request of 4 seats
if userInput == 4:
    if (Row1[2:6] ==["0","0","0","0"]):
        Row1[2:6] = ["1","1","1","1"]
        print("Alloted Seats are: 1c, 1d, 1e, 1f")
    elif (Row1[0:2]==["0","0"] and (Row1[6:] ==["0","0"])):
        Row1[0:2] = ["1","1"]
        Row1[6:] = ["1","1"]
        print("Alloted Seats are: 1a, 1b, 1g, 1h")
    else:
        print("Seats as per plan has been filled")

#conditions for request of 3 seats
if userInput == 3:
    if (Row1[2:5] ==["0","0","0"]):
        Row1[2:5] = ["1","1","1"]
        print("Alloted Seats are: 1c, 1d, 1e")
    elif (Row2[2:5] ==["0","0","0"]):
        Row2[2:5] = ["1","1","1"]
        print("Alloted Seats are: 2c, 2d, 2e")
    elif (Row3[2:5] ==["0","0","0"]):
        Row3[2:5] = ["1","1","1"]
        print("Alloted Seats are: 3c, 3d, 3e")
    else:
        print("Seats as per plan has been filled")

#conditions for request of 2 seats
if userInput == 2:
    if (Row1[0:2] ==["0","0"]):
        Row1[0:2] = ["1","1"]
        print("Alloted Seats are: 1a, 1b")
    elif (Row1[6:] ==["0","0"]):
        Row1[6:] = ["1","1"]
        print("Alloted Seats are: 1g, 1h")
    elif (Row2[0:2] ==["0","0"]):
        Row2[0:2] = ["1","1"]
        print("Alloted Seats are: 2a, 2b")
    elif (Row2[6:] ==["0","0"]):
        Row2[6:] = ["1","1"]
        print("Alloted Seats are: 2g, 2h")
    elif (Row3[0:2] ==["0","0"]):
        Row3[0:2] = ["1","1"]
        print("Alloted Seats are: 3a, 3b")
    elif (Row3[6:] ==["0","0"]):
        Row3[6:] = ["1","1"]
        print("Alloted Seats are: 3g, 3h")
    else:
        print("Seats as per plan has been filled")

#conditions for request of 1 seat
if userInput == 1:
    temp = 0
    try:
        z1=Row1.index("0")
        if (z1==0):
            print("Alloted Seat is: 1a")
        elif (z1==1):
            print("Alloted Seat is: 1b") 
        elif (z1==2):
            print("Alloted Seat is: 1c")
        elif (z1==3):
            print("Alloted Seat is: 1d")
        elif (z1==4):
            print("Alloted Seat is: 1e")
        elif (z1==5):
            print("Alloted Seat is: 1f")
        elif (z1==6):
            print("Alloted Seat is: 1g")
        elif (z1==7):
            print("Alloted Seat is: 1h")
        Row1[z1] = "1"
        temp=1
    except Exception as e:
        pass
    try:
        if(temp==0):
            z2=Row2.index("0")
            if (z2==0):
                print("Alloted Seat is: 2a")
            elif (z2==1):
                print("Alloted Seat is: 2b") 
            elif (z2==2):
                print("Alloted Seat is: 2c")
            elif (z2==3):
                print("Alloted Seat is: 2d")
            elif (z2==4):
                print("Alloted Seat is: 2e")
            elif (z2==5):
                print("Alloted Seat is: 2f")
            elif (z2==6):
                print("Alloted Seat is: 2g")
            elif (z2==7):
                print("Alloted Seat is: 2h")
            Row2[z2] = "1"
            temp=1
    except Exception as e:
        pass
    try:
        if(temp==0):
            z3=Row3.index("0")
            if (z3==0):
                print("Alloted Seat is: 3a")
            elif (z3==1):
                print("Alloted Seat is: 3b") 
            elif (z3==2):
                print("Alloted Seat is: 3c")
            elif (z3==3):
                print("Alloted Seat is: 3d")
            elif (z3==4):
                print("Alloted Seat is: 3e")
            elif (z3==5):
                print("Alloted Seat is: 3f")
            elif (z3==6):
                print("Alloted Seat is: 3g")
            elif (z3==7):
                print("Alloted Seat is: 3h")
            Row3[z3] = "1"
            temp=1
    except Exception as e:
        print("Seats as per plan has been filled")