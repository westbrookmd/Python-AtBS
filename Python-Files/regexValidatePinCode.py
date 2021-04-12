import re

def validate_pin(pin):
    #return true or false
    #pinRegex = re.compile(r'/^\d{4}(?:\d{2})?$/')
    pinRegex = re.compile(r'\d{4}(?:\d{2})?$')
    print (pin)
    val = pinRegex.match(pin)
    print (val)
    try:
        if val.group() == pin and val is not None:
            return True
    except:
        return False

validate_pin("1234")
validate_pin("098765")
