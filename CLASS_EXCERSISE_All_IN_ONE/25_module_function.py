"""
modules 
    create python module unit_converter.py  which has below functions 
        function to convert inch to Foot
        function to convert inch to Meter
        function to convert inch to KiloMeter
        function to convert inch to Mile 
    """
    
def toFoot(inch):
    foot = inch / 12
    return foot    

def toMeter(inch):
    meter = 39.37 * inch
    return meter

def toKilometr(inch):
    kilometr = 39370.0787 * inch
    return kilometr

def toMile(inch):
    mile = 63360 * inch
    return mile