"""
write a program to display name of the month from given month no using if elif and if else 
    """
month =  {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
num = int(input("Enter your month number : "))
print(month.get(num, "invalid num"))   