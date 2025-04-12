"""
	1	2	3	4	5	
1	*					
2	*	*				
3	*	*	*			
4	*	*	*	*		
5	*	*	*	*	*	

    """
# n = 5       
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print() 
""" 
    0  1  2  3  4   
 0              *
 1           *  *
 2        *  *  * 
 3     *  *  *  *
 4  *  *  *  *  *
 
     """
# n = 5       
# for i in range(n):
#     for j in range(i,n):
#         print("*", end="")
#     print()     


# n = 5
# for i in range(n):
    
#     for j in range(i,n):
#         print(" ", end=" ")
       
#     for j in range(i):
#         print("*", end=' ')
  
#     for j in range(i+1):
#         print("*", end = ' ')
#     print()                

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*", end=' ')
#     print()    

# n = 5
# for i in range(n):
    
#     for j in range(i+1):
#         print(" ", end='')
#     for j in range(i,n):
#         print("*", end='')
#     print()

# n = 5
# for i in range(n):
    
#     for j in range(i+1):
#         print(" ", end='')
#     for j in range(i,n-1):
#         print("*", end='')
#     for j in range(i,n):
#         print("*", end='')
        
#     print()                       

# n = 5
# for i in range(n):
    
#     for j in range(i+1):
#         print("", end=' ')
#     for j in range(i):
#         print("*",end=' ')
#     for j in range(i,n):
#         print("*", end=' ')
#     print()            

# n = 5 
# for i in range(n-1):
    
#     for j in range(i,n):
#         print(" ", end='')
#     for j in range(i):
#         print("*", end='')
#     for j in range(i+1):
#         print("*", end='')
#     print()
# for i in range(n):
    
#     for j in range(i+1):
#         print(" ", end='')
#     for j in range(i,n-1):
#         print("*",end='')
#     for j in range(i,n):
#         print("*", end='')
#     print()                         

# n = 4
# for i in range(n-1):
    
#     for j in range(i+1):
#         print(" ", end='')
#     for j in range(i,n-1):
#         print("*", end='')
#     for j in range(i,n):
#         print("*", end='')
#     print()  
    
# for i in range(n):
    
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i):
#         print("*",end='')
#     for j in range(i+1):
#         print("*",end='')
#     print()           
# n = 5
# for i in range(n):
#     print('*')

# n = 4
# for j in range(n):
#     print("*",end=' ')

# n = 5
# for i in range(n):
    
#     for j in range(i+1):
#         print("*", end='')
#     for j in range(i):
#         print(" ",end='')
#     for j in range(i-1):
#         print("*",end='')    
#     print() 
           
           
# n = 5
# for i in range(n):
#     for j in range(n):
        
#         if i == 0 or j==0 or i==n-1 or j==n-1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()                       


# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end='')
#     for j in range(i):    
#         print(" ", end='')
#     for j in range(i+1):    
#         print(" ", end='')    
        
#     if i==n-1 or i==j or i+j==n-1:
#            print("*", end=' ')
#     else:
#            print(" ", end=' ')
#     print()          

# n = 5
# for i in range(n):
    
#     for j in range(i,n):
#         print(" ", end=' ')
#     for j in range(i):
#         if i==n-1 or j==0:
#             print("*", end=' ')
#         else:
#             print(" ",end=' ')    
#     for j in range(i+1):
#         if i==n-1 or i==j:
#             print("*", end=' ')
#         else:
#             print(" ",end=' ')      
#     print()            
                
                
# n = 5
# for i in range(n):
    
#     for j in range(i+1):
#         print(" ", end=' ')
#     for j in range(i,n-1):
#         if i==j or i==0:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     for j in range(i,n):
#         if i==0 or i+j==n-1:
#              print("*",end=' ')
#         else: 
#             print(" ",end=' ')
#     print()   
    
# n = 5
# for i in range(n-1):
    
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i):
#         if j==0:
#              print("*",end='')  
#         else:
#              print(" ",end='')       
#     for j in range(i+1):
#         if i==j:
#             print("*",end='')          
#         else:
#             print(" ",end='')  
#     print()
# for i in range(n):
    
#     for j in range(i+1):
#          print(" ",end='')  
#     for j in range(i,n-1):
#         if i==j:
#              print("*",end='')  
#         else:
#              print(" ",end='')   
#     for j in range(i,n):
#         if i+j==n-1:
#              print("*",end='')  
#         else:
#              print(" ",end='')  
#     print()                                                

# n = 5
# for i in range(n-1):
    
#     for j in range(i+1):
#         print(" ",end='')
#     for j in range(i,n-1):
#         if i==0 or i==j:
#             print("*",end='')
#         else:
#             print(" ",end='')   
#     for j in range(i,n):
#         if i==0 or i+j==n-1:
#              print("*",end='')
#         else:
#             print(" ",end='')   
#     print()                     
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i):
#         if i==n-1 or i+j==n-1:
#             print("*",end='') 
#         else:
#             print(" ",end='')
#     for j in range(i+1):
#         if i==n-1 or i==j:
#             print("*",end='') 
#         else:
#             print(" ",end='')    
#     print()                           

# n = 5
# for i in range(n-1):
    
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i):
#         if j==0:
#             print("*",end='')
#         else:
#             print(" ",end='') 
#     for j in range(i+1):
#         if j==i:
#             print("*",end='')
#         else:
#             print(" ",end='') 
#     print()  
# for i in range(n):
    
#     for j in range(i+1):
#         print(" ",end='')    
#     for j in range(i,n-1):
#         if j==i:
#             print("*",end='')
#         else:
#             print(" ",end='')  
#     for j in range(i,n):
#         if j==4:
#              print("*",end='')
#         else:
#             print(" ",end='')   
#     print()     
    
    
# n = 5
# for i in range(n-1):
    
#     for j in range(i+1):
#         print(" ",end='')    
#     for j in range(i,n-1):
#         if i==0 or j==i:
#             print("*",end='')
#         else:
#             print(" ",end='')  
#     for j in range(i,n):
#         if i==0 or j==4:
#              print("*",end='')
#         else:
#             print(" ",end='')   
#     print()     
# for i in range(n):
    
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i):
#         if i==n-1 or j==0:
#             print("*",end='')
#         else:
#             print(" ",end='') 
#     for j in range(i+1):
#         if i==n-1 or j==i:
#             print("*",end='')
#         else:
#             print(" ",end='') 
#     print()          


n = 5
p = 1
for i in range(1,n):
    for j in range(i):
        print(p,end=' ')
        p=p+1
    print()


# n = 9
# p = 1          
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end='')
     
#     for j in range(i):
#         print(p,end='')
    
    
#     for j in range(i+1):
#          print(p,end='')
#     p+=1
#     print() 

# n = 9
# p = 1          
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end='')
     
#     for j in range(i):
#         print(i+1,end='')
       
    
#     for j in range(i+1):
#         print(i+1,end='')
#     print() 

# n = 9
        
# for i in range(n):
#     p = 1  
#     for j in range(i,n):
#         print(" ",end='')
     
#     for j in range(i):
#         print(p,end='')
       
    
#     for j in range(i+1):
#         print(p,end='')
#         p=p+1
#     print() 
       
       