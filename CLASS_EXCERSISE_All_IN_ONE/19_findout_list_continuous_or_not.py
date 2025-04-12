"""
 write a program to findout whether list is continuous or not 
    list1 = [10,11,12,13,14,15] it is continuous list 
    list1 = [10,11,12,14,15,16] it is not continuous list 

"""
list = [10,11,12,13,14,15]  
for i in range(len(list)-1):
    if list[i] + 1 != list[i+1]:
        print("it is not continuous list")
        break
else:   
    print("it is continuous list")
    
    
list1 = [10,11,12,14,15,16]     
for i in range(len(list1)-1):
    if list1[i] + 1 != list1[i+1]:
        print("it is not continuous list")
        break  
else:   
    print("it is continuous list")
        