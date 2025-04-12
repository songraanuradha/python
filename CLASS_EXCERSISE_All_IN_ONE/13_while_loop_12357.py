"""
1 2 3 5 7 11 13 17 19 ....... 10000
    """
    
for j in range (1,10000):
    is_prime = True
    if (j==1 or j==2):
        is_prime = True
    else:
        for i in range (2,j//2):
            if j%i ==0:
                is_prime = False
                break
    if is_prime:
                print(j , end=' ')
                
      
                
        

