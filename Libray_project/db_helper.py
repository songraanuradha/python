"""
1)inport
2)function(modify)

    """
import connection as con  
import mysql.connector as conneter
import sys
  
def modify(sql,values):
    try: 
        mycurser = con.database.cursor()
        
        mycurser.execute(sql,values)
        
        con.database.commit()
        
    except conneter.errors as e :
        print(e.msg)
    
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
         

    