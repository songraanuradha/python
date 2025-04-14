import mysql.connector as connector
import connectivity as con
import sys

def modify(sql,values):
   
    try:    
        command = con.database.cursor()
        command.execute(sql,values)
        con.database.commit()
        
        count = command.rowcount
        return count
    except connector.Error as err:
            print("Database error occurred:", err)
            return 0
    except Exception as e:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Details:", e)
            return 0   
        
def fetch(sql,data=None):
    
    try:
        command = con.database.cursor(dictionary=True)
        if data!= None:
            print(data)
            command.execute(sql,data)
        else:
            command.execute(sql)
        return command.fetchall()
    except connector.Error as err:
            print("Database error occurred:", err)
            return 0
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()                