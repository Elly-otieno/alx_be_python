def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError('Division by zero is not allowed')
        return x/y
    except TypeError as e:
        print(e)

print(divide(7,0))