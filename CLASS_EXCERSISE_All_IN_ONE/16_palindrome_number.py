"""
write a program to check whether given number is palindrome or not
input : 1331 reverse 1331 

    """



num = int(input("Enter a number : "))
acutal_num = num
reverse_num = 0
while num>0:
    digit = num%10
    reverse_num = reverse_num*10+digit
    num = num//10
print("reverse number", reverse_num)


if(acutal_num==reverse_num):
    print("palidrom number")
else:
    print("not palindrom number")
