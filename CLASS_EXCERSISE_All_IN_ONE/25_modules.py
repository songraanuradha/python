"""modules 
    create python module unit_converter.py  which has below functions 
        function to convert inch to Foot
        function to convert inch to Meter
        function to convert inch to KiloMeter
        function to convert inch to Mile 
"""


import example
inch = float(input("Enter inch : "))
foot = example.toFoot(inch)
meter = example.toMeter(inch)
kilometer = example.toKilometr(inch)
mile = example.toMile(inch)
print(f"foot = {foot} Meter = {meter} Kilometer = {kilometer} Mile = {mile}")
