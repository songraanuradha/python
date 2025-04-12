"""
 create python module AmountToWords.py which has below function 
        function to convert amount into words (toWords)
            input : 123 output one two three 
        function to convert amount in words to digit (toAmount)
            input : one two three 
            output : 123
    """
    
    
def toAmount_into_rupee(words):
    if words == 1:
        print("one")
        
    elif words == 2:
        print("Two")
        
    elif words == 3:
        print("Three")
        
    else:
        print("Thank you")      
           