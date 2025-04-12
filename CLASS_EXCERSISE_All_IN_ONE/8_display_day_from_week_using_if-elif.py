"""
write a program to accept day of week from user. and display name of the day using if elif and if else 

    """
day = int(input("Enter your day : ")) 
if day<=0 or day>7:
    print("Invalid input")  

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")    
elif day == 3:
    print("Wednesday")    
elif day == 4:
    print("Thuresday")    
elif day == 5:
    print("Friday")    
elif day == 6:
    print("Satursday")    
elif day == 7:
    print("Sunday") 
else:
    print("Thank you")       