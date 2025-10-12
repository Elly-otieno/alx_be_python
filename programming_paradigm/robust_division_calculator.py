def safe_divide(numerator, denominator):
    try:
        if float(denominator) == 0:
            raise ZeroDivisionError('Error: Cannot divide by zero.')
        return float(numerator) / float(denominator)
    except ValueError:
        return 'Error: Please enter numeric values only.'