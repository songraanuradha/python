import mysql.connector as connector
import connectivity as con
import sys

def modify(sql,values):
   
    try:    
        mycurser = con.database.cursor()
        mycurser.execute(sql,values)
        con.database.commit()
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()    
        
def fetch(sql,data=None):
    
    try:
        connection = con.database.cursor(dictionary=True)
        if data!= None:
            print("dat")
            connection.execute(sql,data)
        else:
            connection.execute(sql)
            return connection.fetchall()
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()                