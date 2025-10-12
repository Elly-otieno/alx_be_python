class ValueTooHighError (Exception):
    '''takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Sorry '{self.value}' is too high"
    
def value_too_high(value):
    try:
        if value > 100:
            raise ValueTooHighError(value)
        return f'{value} is within allowed limits'
    except ValueError as e:
        return e
    
print(value_too_high('ieqyuidajhs'))