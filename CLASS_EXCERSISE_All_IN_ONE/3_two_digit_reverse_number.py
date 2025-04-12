"""
3) write a program to accept two digit amount from user and reverse it (as number)
input : 45 output 54
input : 29 output 92
"""

int= int(input("Enter the number : "))
num1 = int % 10
num2 = int // 10
print( f"{num1}{num2}")