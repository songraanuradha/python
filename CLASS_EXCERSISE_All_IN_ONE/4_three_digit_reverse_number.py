"""
4) write a program to accept 3 digit amount from user and reverse it (as number)
input : 145 output 541
input : 298 output 892
"""

int = int(input("Enter the number : "))
num1 = int % 10
num2 = int // 10
num3 = num2 % 10
num4 = int // 100
print(f"{num1}{num3}{num4}")
