"""
write a program to check whether given number is composite number or not 

The composite numbers up to 100 are listed below. 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100

 1: get input from uder
 2:chech numbe is compositr or not
 3:print

    """
num = int(input("Enter the number"))
if num<4:
    print("invalid input")
else:
    i = 2
    i
          






























# if num<=3:
#     print("Enter valid number")
    
# else:
# for j in range (1,100):
#     is_prime = True
#     if (j==1 or j==2 or j==3):
#         is_prime = False
#     else:
#         for i in range (2,j//2):
#             if j%i ==0:
#                 is_prime = True
#                 break
#     if is_prime:
#                 print(j , end=' ')

number = int(input("Enter number to check is compositr or not")) 
count=0
if number!=2 and number%2==0:
    print(f"{number} is composite num")
else:
    divisor = 2 
    half = number // 2
    while divisor<half:
        count+=1
        reminder = number%divisor 
        if reminder==0:
            print(f"{number}  is composite num ")
            break
        divisor=divisor+1
    if  divisor==half or number==2:
        print(f"{number} is not composite num")
print(count)
     