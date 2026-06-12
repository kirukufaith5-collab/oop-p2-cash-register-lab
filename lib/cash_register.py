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

    def add_item(self, item_name, price, quantity=1):
        """
        Adds item names to self.items multiplied by quantity, 
        updates the running total, and logs the transaction.
        """
        # 1. Calculate the line total for this specific item batch
        line_total = price * quantity
        self.total += line_total

        # 2. Add the item name to your items list 'quantity' times
        for _ in range(quantity):
            self.items.append(item_name)

        # 3. Log the record into previous transactions (matching key names)
        transaction_record = {
            "item": item_name,  # Changed to "item" to match void_last_transaction
            "price": price,
            "quantity": quantity,
            "line_total": line_total
        }
        self.previous_transactions.append(transaction_record)

    def apply_discount(self):
        multiplier = (100 - self.discount) / 100
        self.total = self.total * multiplier

    def void_last_transaction(self):
        # Checks if there are any transactions to undo
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Pop the last logged transaction
        last_transaction = self.previous_transactions.pop()
        
        # Deduct its cost from the register total
        self.total -= last_transaction["line_total"]
        
        # Remove the items from your list 'quantity' times
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])


if __name__ == "__main__":
    user_raw_input = input("Enter discount: ").strip()
    
    if user_raw_input == "":
        register = CashRegister()
    else:
        register = CashRegister(user_raw_input)

    print(f"\n--- Register Initialized with a {register.discount}% discount plan ---")