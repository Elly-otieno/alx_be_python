shopping_list = ['mangoes']

item_found = False

while not item_found:
    item = input('Enter item to search or q to quit: ')

    if item.lower() == "q":
        print('You have excited the search')
        break
    if item in shopping_list:
        item_found = True
        print(f'{item} is in your shopping list')
    else:
        print(f'{item} is not in your shopping list')