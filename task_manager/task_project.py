import sys
import function as fun

def getfun():
        title = input("Enter your task title : ")
        person = input("Enter your task person : ")
        start_date = input("Enter date start_date : ")
        end_date = input("Enter date end_date : ")
        status = input("Enter your task status (0 = Pedding, 1 = Done) : ")
        description = input("Enter your task description : ")
        return title,person,start_date,end_date,status,description  

def showTasks(sql,data=None):
       
        tables = fun.fetch(sql,data)
        count = len(tables)
        # print(tables)
        if count == 0:
                print("no task found")
        else:
        
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{'id':<5} {'title':<34} {'person':<20} {'start_date':<15} {'end_date':<15} {'status':<12} {'description':<42}")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                for row in tables:
                        date_string = row['start_date'].strftime("%Y-%m-%d")
                        date_string2 = row['end_date'].strftime("%Y-%m-%d")
                        msg = ''
                        if row['status'] == 0:
                                msg = 'Pedding'
                        else:
                                msg = 'Done'
                                        
                        output = f"{row['id']:<5} {row['title']:<34} {row['person']:<20} {date_string:<15} {date_string2:<15} {row['status']:<12} {row['description']:<42}"
                        print(output)
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                
                print(f"no of tasks is = {count}")
        pause = input('press any key : ')


while 1:
        try:    
                print("Press 1 to view all task")
                print("Press 2 to add new task")
                print("Press 3 to update task")
                print("Press 4 to delete task")
                print("Press 5 to search task by title")
                print("Press 6 to search task by person")
                print("Press 7 to update task status")
                print("Press 0 to exit")
                
                try:
                        choice = int(input("Enter your choice : "))
                        if choice == 0:
                                print("Good bye")
                                break
                        
                        elif choice == 1:
                                
                                print('we will display all task')
                                
                                sql = "select * from tasks order by id "
                                showTasks(sql)
                                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")   
                                
                                
                        elif choice == 2:
                                
                                print('we will insert task')
                                
                                value = getfun()
                                sql = "insert into tasks(title,person,start_date,end_date,status,description)values(%s,%s,%s,%s,%s,%s)"
                                values = [value[0],value[1],value[2],value[3],value[4],value[5]]
                                count = fun.modify(sql,values)
                                if count ==1:
                                        print("task inserted ")
                                else:
                                        print("task not inserted")
                                pause = input('Enter any key : ')                
                                
                                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                
                                
                        elif choice == 3:
                                
                                print('we will update task')
                                
                                sql1 = "select * from tasks order by id "
                                showTasks(sql1)
                                id = int(input("Enter task id to update : ")) 
                                value = getfun()
                                sql2 = "update tasks set title=%s,person=%s,start_date=%s,end_date=%s,status=%s,description=%s where id=%s"
                                data = [value[0],value[1],value[2],value[3],value[4],value[5],id]
                                count = fun.modify(sql2,data)
                                if count == 0:
                                        print('Task not found')
                                else:
                                        print('Task updated')

                                                
                                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                
                                
                                
                        elif choice == 4:
                                
                                print('we will delete task')
                                
                                sql = "select * from tasks order by id "
                                showTasks(sql)
                                try:
                                        deletbyid = int(input("Enter id"))
                                        sql2 = "delete from tasks where id=%s"
                                        data=[deletbyid]
                                        count = fun.modify(sql2,data)
                                        if count==0:
                                                print('tasks not found')
                                        else: 
                                                print('tasks has been deleted successfully')
                                except ValueError:
                                        print("Invalid input. Please enter a numeric ID.")
                                
                                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                
                                
                        elif choice == 5:
                                
                                print('we will search task by title : ')
                                
                                title = input("Enter your task title : ")
                                sql = "select * from tasks where title like %s"
                                data=[f"%{title}%"]
                                showTasks(sql,data)
                                
                                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                
                                
                        elif choice == 6:
                                
                                print('we will search task by person') 
                                
                                person = input("Enter your task person : ")
                                sql = "select * from tasks where person like %s"
                                data=[f"%{person}%"]
                                showTasks(sql,data)
                                
                                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                
                        elif choice == 7:
                                
                                print('we will update task status')
                        
                                sql = "select * from tasks order by id"
                                showTasks(sql)
                                taskID = int(input("Enter task id to update status : ")) 
                                status = input("Enter book status 0 = Pedding, 1 = Done : ")
                                sql = "update tasks set status=%s where id=%s"
                                data = [status,taskID]
                                count = fun.modify(sql,data)
                                if count == 0:
                                        print('Task not found')
                                else:
                                        print('Task updated')
                                
                        else:
                                print('invalid choice')
                except:
                        print("only number between (0 to 7) are allowed")
                        print("Oops!",sys.exc_info()[0],"occured.")
                        print()
            
        except:
                print("invalid input, please enter a number") 