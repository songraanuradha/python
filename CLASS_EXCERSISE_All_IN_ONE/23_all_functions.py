"""
functions
    create function that will filter and returns grains from any number of items 
    
    fun
    list
    grains -> store
    retuen
"""

# def all():
#     item = ['Oats', 'Quinoa', 'Brown Rice', 'Millet', 'Barley', 'Apple', 'Banana', 'Mango', 'Pomegranate', 
#             'Blueberries', 'Chia Seeds', 'Flaxseeds', 'Papaya', 'Strawberries', 'Grapes', 'Kiwi', 
#             'Dates', 'Raisins', 'Figs', 'Watermelon']
#     grains = ['Blueberries', 'Chia Seeds', 'Flaxseeds','fheufbaskj','wuaygfajbfajk']
    
#     for grain in item:
#         if grain in grains:
#          print(grain)
        
    
# all()   

"""
 create function that will return indian state names and from any all asian state names 
"""  
# def all_contry_state():
    
#     state = ['Maharashtra', 'California', 'Karnataka', 'Texas', 'Tamil Nadu', 'New York', 
#             'Gujarat', 'Florida', 'Rajasthan', 'Illinois', 'Uttar Pradesh', 'Pennsylvania', 
#              'West Bengal', 'Ohio', 'Kerala', 'Georgia', 'Punjab', 'North Carolina', 'Bihar', 'Michigan']
    
#     states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 
#             'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 
#             'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 
#             'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 
#             'Uttarakhand', 'West Bengal']

    
#     for indian_state in state:
#         if indian_state in states:
#             print(indian_state)
# all_contry_state()            
        
"""
create function that will return two list one has only odd values and other has only even value 
from any number of values passed in function 

           fun
           list
           %2 = even
           else odd
           even []
           odd []
           print
"""         
def odd_even(*args):
    
    odd_num = []
    even_num = []
    
    for num in args:
        if num % 2==0:
            even_num.append(num)
        else:
            odd_num.append(num)
         
    return odd_num,even_num       

odd_numbers, even_numbers = odd_even(5,6,7,32,45,67)
print(odd_numbers)
print(even_numbers)