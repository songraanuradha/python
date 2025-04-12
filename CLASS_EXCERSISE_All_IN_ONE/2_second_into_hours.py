"""
    2) write a program to accept total seconds from user and convert it into  hours and remaining minutes & remaining seconds
input : 3675 seconds output 1 hour minute 1 seconds 15 

"""
sec = int(input("Enter you number :"))
hour = sec//3600
min = sec%3600
min = min//60
second = sec%60
print(f"{hour} hour {min} minute {second} seconds")
        
    
    