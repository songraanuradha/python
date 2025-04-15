"""
1) add all features
2)choice
3)try except

"""
import sys
import db_helper as db


def getinput():
        title = input("Enter your tittle : ")
        author = input("enter your autheor name : ")
        genre = input("enter your genretion : ")
        year = int(input("enter your year : "))
        status = int(input("entr your status (1=owned, 2 = borrowed) : "))
        return title,author,genre,year,status
def showBooks(sql,data=None):
        
        
       
                                
        tables = db.fetch(sql,data)
        count = len(tables)
        if count == 0:
                print('no books found')
        else:        
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print(f"{'id':<5} {'title':<40} {'author':<32} {'genre':<32} {'year':<8} {'status':<10}")
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                for row in tables:
                        msg = ''
                        if row['status'] == 1:
                                msg = 'purchased'
                        else:
                                msg = 'borrowed'
                                        
                        output = f"{row['id']:<5} {row['title']:<40} {row['author']:<32} {row['genre']:<32} {row['year']:<8} {row['status']:<10}"
                        print(output)
                print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')        
                
                print(f"no of books in your libarary = {count}") 
        pause = input("Enter any key")
while  1:
        try:
                print('press 1 to view all books')
                print('press 2 to add new book')
                print('press 3 to update book')
                print('press 4 to delete book')
                print('press 5 to search book by tittle')
                print('press 6 to search book bt auther')
                print('press 7 to update book status')
                print('preess 0 to exit')
                try:
                                choice = int(input("Enter your choice : "))
                                if choice == 0:
                                        print('Good bye')
                                        break
                                elif choice == 1:
                                                print('we will display all book')
                                                sql = "select * from books order by id"
                                                showBooks(sql)  
                                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                                                
                                elif choice == 2:
                                                print('we will insert book')
                                                value = getinput()
                                                sql = "insert into books(title,author,genre,year,status) values(%s,%s,%s,%s,%s)"
                                                data = [value[0],value[1],value[2],value[3],value[4]]
                                                count = db.modify(sql,data)
                                                if count == 0:
                                                        print('book not inserted')
                                                else:
                                                        print('book inserted successfully')
                                                pause = input('enter any key') 
                                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                                                
                                                        
                                elif choice == 3:
                                                print('we will update book')
                                                
                                                sql = "select * from books order by id"
                                                showBooks(sql)
                                                
                                                id = int(input("Enter book id"))
                                                value = getinput()
                                        
                                                sql = "update books set title=%s,author=%s,genre=%s,year=%s,status=%s where id=%s"
                                                data = [value[0],value[1],value[2],value[3],value[4],id]
                                                count = db.modify(sql,data)
                                                if count == 0:
                                                        print('book not found')
                                                else:
                                                        print('book updated successfully')
                                                
                                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")        
                                                
                                elif choice == 4:
                                                print('we will delete book')
                                                
                                                sql = "select * from books order by id"
                                                showBooks(sql)
                                                bookid = int(input("Enter book id"))
                                                sql2 = "delete from books where id=%s"
                                                data=[bookid]
                                                count = db.modify(sql2,data)
                                                if count == 0:
                                                        print('book not found')
                                                else:
                                                        print('book will deleted successfilly')   
                                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")              
                                                
                                elif choice == 5:
                                                print('we will search book by tittle ')
                                                
                                                title = input("Enter your tittle : ")
                                                sql = "select * from books where title like %s"
                                                data = [f"%{title}%"]        
                                                showBooks(sql,data)
                                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                                                                
                                elif choice == 6:
                                                print('we will search book by auther')
                                                
                                                author = input("Enter your auther name : ")
                                                sql = "select * from books where author like %s"
                                                data = [f"%{author}%"]
                                                showBooks(sql,data)
                                                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------") 
                                                
                                                
                                elif choice == 7:
                                                print('we will update book status')
                                                
                                                sql = "select * from books order by id"
                                                showBooks(sql)
                                                bookID = int(input("Enter book id"))
                                                status = int(input("Enter your status (1=purchased, 2 = borrowed) : "))
                                                sql = "update books set status=%s where id=%s"
                                                data = [status,bookID]
                                                count = db.modify(sql,data)
                                                if count == 0:
                                                        print('book not found')
                                                else:
                                                        print('book status updated successfully')
                                                
                                else:
                                                print('invalid choice') 
                except:
                        print("Oops!",sys.exc_info()[0],"occured.")
                        print("Next entry.")
                        print()
        except:
                print("invalid input, please enter valid input")       
                
        
        
        
        
        
        
        
        
        
        
        
        
        
