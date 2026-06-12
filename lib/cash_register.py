#!/usr/bin/env python3

class CashRegister:
  
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        
        try:
            cleaned_value = int(value)
        except (ValueError, TypeError):
            print("Not valid discount")
            self._discount = 0
            return

        if 0 <= cleaned_value <= 100:
            self._discount = cleaned_value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity):
        line_total = price * quantity
        self.total += line_total
        self.items.append(item)
        
        transaction_record = {
            "item": item,
            "price": price,
            "quantity": quantity,
            "line_total": line_total
        }
        self.previous_transactions.append(transaction_record)

    def apply_discount(self):
        multiplier = (100 - self.discount) / 100
        self.total = self.total * multiplier

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["line_total"]
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

if __name__ == "__main__":
    
    user_raw_input = input("Enter discount: ").strip()
    
    
    if user_raw_input == "":
        register = CashRegister()
    else:
        register = CashRegister(user_raw_input)

    print(f"\n--- Register Initialized with a {register.discount}% discount plan ---")
  pass
