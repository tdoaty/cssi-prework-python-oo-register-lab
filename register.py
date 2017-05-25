class CashRegister:
    def __init__ (self, discount= 0):
        self.discount = discount
        self.total = 0
        self.items = []
    def add_item(self, item, price, quantity = 1):
        self.last_quantity = quantity
        self.last_price_total = (price * quantity)
        for i in range(quantity):
            self.items.append(item)
        self.total += (price * quantity)
    def apply_discount(self):
        if self.discount > 0:
            quotient = self.discount / 100.00
            self.total = self.total - (quotient * self.total)
            return "After the discount, the total comes to $%.2f."
        else:
           return "There is no discount to apply."
     def void_last_transaction(self):
         self.total -= self.last_price_total
         for i in range(self.last_quantity):
              self.items.pop()
