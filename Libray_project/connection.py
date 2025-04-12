# connectivity

import mysql.connector as con
import sys

try: 
    database = con.connect(host = 'localhost', user = 'root',password= '',database= 'book_library',port=3306)
    print('succesfully connnect ')
except:
    print("Oops!",sys.exc_info()[0],"occured.")
    print("Next entry.")
    print()
 