"""
write a program to findout whether all the words in list are starting with vowels or not 

    friends1 = ['Asha','Priti','Sheela','Mona','Radha'] list has friends not starting with vowels
    friends2 = ['Aarohi','Oli','Ela'] list has friends not with vowels
"""

friends1 = ['Asha','Priti','Sheela','Mona','Radha']
for i in friends1:
    if i[0].lower() not in 'aeiou':
        print(f" {friends1} list has friends not starting with vowels")
        break
else:   
    print( f" {friends1} list has friends starting with vowels")
    
print("--------------------------------------------------------------------------------------------")    
    
friends2 = ['Aarohi','Oli','Ela']
for i in friends2:
    if i[0].lower() not in 'aeiou':
        print(f" {friends2} list has friends not starting with vowels")
        break
else:   
    print(f" {friends2} list has friends starting with vowels")   