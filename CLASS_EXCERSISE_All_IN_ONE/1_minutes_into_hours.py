"""
1) write a program to accept total minutes from user and convert it into  hours and remaining minutes
input : 150 minutes output 2 hours 30 minutes 

"""
min = int(input("Enter you number : "))
hour = min//60
min = min%60
print(f"{hour} hours {min} minutes")

