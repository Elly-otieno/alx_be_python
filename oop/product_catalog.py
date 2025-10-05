class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
product1 = Product('Orange', 12, 46)
print(f"Product: {product1.name}, Total Value: Ksh {product1.total_value()}")