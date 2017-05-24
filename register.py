class CashRegister:
    def __init__ (self, discount= 0):
        self.discount = discount
        self.total = 0
        self.items = []
    def add_item(self, item, price, quantity = 1):
        for i in range(quantity):
            self.items.append(item)
        self.total += (price * quantity)
    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total - ((self.discount / 100) * self.total)
            return "After the discount, the total comes to " + str(self.total) + "."
        else:
           return "There is no discount to apply."
     def void_last_transaction(self):
         self.recent_item_total = self.total + (price * quantity)
         self.recent_item_quantity += quantity
         for i in range(self.item_recent_item_quantity):
              self.items.pop()
