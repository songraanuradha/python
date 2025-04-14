"""
1)inport
2)function(modify)

    """
import connection as con  
import mysql.connector as conneter
import sys
  
def modify(sql,data):
    try: 
        command = con.database.cursor()
        
        command.execute(sql,data)
        
        con.database.commit()
        count = command.rowcount
        return count
        
    except conneter.errors as e :
        print(e.msg)
        print("value error")
        return -1
    
def fetch(sql,data=None):
    try:   
        command = con.database.cursor(dictionary=True)
        if data!= None:
            print(data)
            command.execute(sql,data)
        else:
            command.execute(sql)
        return command.fetchall()
    except:    
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
         

    