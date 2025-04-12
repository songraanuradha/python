"""
decision making 
------------------
    simple decision making if  
        2) write a program to decide type of shape (square,portrait, landscape) from given length and width 
"""
length = int(input("Enter the number : "))
width = int(input("Enter the number : "))

if length == width:
    print("square")
    
if length < width:
    print("landscape")
    
if  length > width:  
    print("portrait") 
    
if  length and  width <= 0:
    print()   
     
