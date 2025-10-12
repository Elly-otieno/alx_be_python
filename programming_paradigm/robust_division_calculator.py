def safe_divide(numerator, denominator):
    try:
        if float(denominator) == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return float(numerator) / float(denominator)
    except ValueError:
        return 'Please enter numeric values only'