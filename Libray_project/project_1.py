"""
1) add all features
2)choice
3)try except

"""
import sys

import db_helper as db
def showBooks():
        sql = "select * from books order by id desc"
                                
        tables = db.fetch(sql)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"{'id':<5} {'title':<64} {'author':<32} {'genre':<32} {'year':<8} {'status':<10}")
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        for row in tables:
                output = f"{row['id']:<5} {row['title']:<64} {row['author']:<32} {row['genre']:<32} {row['year']:<8} {row['status']:<10}"
                print(output)
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')        
        count = len(tables)
        print(f"no of books in your libarary = {count}") 
        pause = input("Enter any key")
while  1:
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
                                showBooks()  
                                
                                
                elif choice == 2:
                                print('we will insert book')
                                title = input("Enter your tittle : ")
                                author = input("enter your autheor name : ")
                                genre = input("enter your genretion : ")
                                year = int(input("enter your year : "))
                                status = int(input("entr your status (1=owned, 2 = borrowed) : "))
                                sql = "insert into books(title,author,genre,year,status) values(%s,%s,%s,%s,%s)"
                                values = [title,author,genre,year,status]
                                count = db.modify(sql,values)
                                if count == 0:
                                        print('book not inserted')
                                else:
                                        print('book inserted successfully')
                                pause = input('enter any key')              
                elif choice == 3:
                                print('we will update book')
                                
                elif choice == 4:
                                print('we will delete book')
                                showBooks()
                                bookid = int(input("Enter book id"))
                                sql = "delete from books where id=%s"
                                data=[bookid]
                                count = db.modify(sql,data)
                                if count == 0:
                                        print('book not found')
                                else:
                                        print('book will deleted successfilly')        
                                
                elif choice == 5:
                                print('we will search book by tittle ')
                                
                elif choice == 6:
                                print('we will search book by auther')
                                
                elif choice == 7:
                                print('we will update book status')
                else:
                                print('invalid choice') 
    except:
                print("Oops!",sys.exc_info()[0],"occured.")
                print("Next entry.")
                print()
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        