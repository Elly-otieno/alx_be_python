class OutOfStockError(Exception):
    """ Custom exception for handling out of stock items"""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock"
    
# sample inventory
product_iventory = {
    "apple" : 10,
    "banana" : 5,
    "orange" : 0,
    "grapes" : 3
}

def purchase_item(item, quantity):
    try:
        if quantity == 0:
            print(f"Sorry you cannot purchase {quantity} number of {item}s")
        else:
            if product_iventory[item] == 0:
                raise OutOfStockError(item)
            else:
                print(f"Purchase succesful: {quantity} {item}(s)")
                product_iventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not in our inventory")



# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
except OutOfStockError as e:
    print(e)  # Output: