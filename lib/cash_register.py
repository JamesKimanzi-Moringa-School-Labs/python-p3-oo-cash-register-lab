class CashRegister:
    def __init__(self, discount=0):
        self.items = []
        self.last_transaction = 0
        self.total = 0
        self.discount = discount

    def add_item(self, item_name, price, quantity=1):
        self.items.append({"item_name": item_name, "price": price, "quantity": quantity})
        self.last_transaction = price * quantity
        self.total += self.last_transaction

    def apply_discount(self):
        if self.discount > 0 and self.discount <= 100:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return "After discount: ${:.2f}".format(self.total)
        else:
            return "Invalid discount percentage"

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction
            del self.items[-1]
            self.last_transaction = 0
        else:
            return "No transactions to void"


# Testing the CashRegister class
register_without_discount = CashRegister()
register_without_discount.add_item("Apple", 1.50, 2)
register_without_discount.add_item("Banana", 0.75)
print("Total without discount:", register_without_discount.total)  

register_with_discount = CashRegister(20)
register_with_discount.add_item("Apple", 1.50, 2)
register_with_discount.add_item("Banana", 0.75)
print("Total before discount:", register_with_discount.total)  
print(register_with_discount.apply_discount())  

register_with_discount.void_last_transaction()
print("Total after voiding last transaction:", register_with_discount.total) 