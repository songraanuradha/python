"""
recursion
    write a program to find & display octal of given decimal number 
    write a program to find & display hexadecimal of given decimal number 


"""

# 1)  write a program to find & display octal of given decimal number 

# def decimal_to_octal(n):
#     if n == 0:    

#         return ''
#     else:
#         return decimal_to_octal(n // 8) + str(n % 8)

# decimal_number = 100
# octal_number = decimal_to_octal(decimal_number)           
# print(f"The octal of {decimal_number} is: {octal_number}")

                               
# 2)  write a program to find & display hexadecimal of given decimal number
def decimal_to_hexadecimal(n):    
    if n == 0:
        return ''
    else:
        hex_digits = '0123456789ABCDEF'
        return decimal_to_hexadecimal(n // 16) + hex_digits[n % 16]

decimal_number = 100
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print(f"The hexadecimal of {decimal_number} is: {hexadecimal_number}")


    