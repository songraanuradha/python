import sys
import function as fun
def showTasks():
        sql = "select * from tasks order by id "
        tables = fun.fetch(sql)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"{'id':<5} {'title':<44} {'description':<42} {'due_date':<32} {'status':<8}") 
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        for row in tables:
                output = f"{row['id']:<5} {row['title']:<44} {row['description']:<42} {row['due_date']:<32}  {row['status']:<8}"
                print(output)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        count = len(tables)
        print(f"no of tasks is = {count}")
        pause = input('press any key')


while 1:
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
                showTasks()
                
        elif choice == 2:
                print('we will insert task')
                title = input("Enter your task title : ")
                description = input("Enter your task description : ")
                due_date = input("Enter date : ")
                status = int(input("Enter your task status (0 = Pedding, 1 = Done) : "))
                pause = int(input("press any key"))
                
                sql = ("insert into tasks(title,description,due_date,status)values(%s,%s,%s,%s)")
                values = [title,description,due_date,status]
                count = fun.modify(sql,values)
                
                if count ==1:
                        print("task inserted se")
                
        elif choice == 3:
                print('we will update task')
                
        elif choice == 4:
                print('we will delete task')
                showTasks()
                deletbyid = int(input("Enter id"))
                sql = "delete from tasks where id=%s"
                data=[deletbyid]
                count = fun.modify(sql,data)
                if count==0:
                   print('tasks not found')
                else: 
                   print('tasks has been deleted successfully')
                
        elif choice == 5:
                print('we will search task by title')
                
        elif choice == 6:
                print('we will search task by person')
                
        elif choice == 7:
                print('we will update task status')
        else:
                print('invalid choice')
    except:
        print("only number between (0 to 7) are allowed")
        print("Oops!",sys.exc_info()[0],"occured.")
        print()
            
   