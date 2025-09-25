number = int(input('Enter a number to see its multiplication table: '))
# multiplier = [1,2,3,4,5,6,7,8,9,10]                    

for multiple in range(1,11) :
    result = number * multiple
    print(f'{number}*{multiple}={result}')
