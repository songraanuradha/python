import sys
import mysql.connector as connector


try:
    database = connector.connect(host = 'localhost',user= 'root',password ='',database='simple_task_manager',port=3306)
    print('connection successfully')
except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()


    