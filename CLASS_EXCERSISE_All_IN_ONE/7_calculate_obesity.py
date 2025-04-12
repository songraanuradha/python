"""if else ladder decision making statement
        1) write a program to calculate bmi and display obesity level of person from given height
         (foot and inch) and weight.
         
         BMI = kg/meter^2 # BMI = kg /(meter**2)
        Underweight: BMI below 18.5 
        Normal weight: BMI between 18.5 and 24.9 
        Overweight: BMI between 25 and 29.9 
        Obese: BMI of 30 or higher '''
        
        1 inch = 0.0254meter,1 foot = 0.3048 meter
"""

height =  int(input("Entre your height(inch) : "))
weight =  int(input("Entre your weight : "))

meter =( height*0.0254) 

BMI = weight/(meter**2 )

if BMI>=30:
    print(" your obesity level is : Obese")
    
elif BMI>=25:
    print(" your obesity level is : Overweight")
    
elif BMI>=18:
    print(" your obesity level is :  Normal weight")
    
else:
    print(" your obesity level is : Underweight")
    
    
            





