"""
write a program to display name of the month from given month without using decision making
month =  {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
    """
month = int(input("Enter your month number"))
if month<=0 or month>12:
    print("invalid month number")   
else:
    if month == 1:
        print("January")   
    elif month == 2:
        print("February")   
    elif month == 3:
        print("March")   
    elif month == 4:
        print("April")   
    elif month == 5:
        print("May")   
    elif month == 6:
        print("June")   
    elif month == 7:
        print("July")   
    elif month == 8:
        print("August")   
    elif month == 9:
        print("September")   
    elif month == 10:
        print("October")   
    elif month == 11:
        print("November")   
    elif month == 12:
        print("December")   
        
