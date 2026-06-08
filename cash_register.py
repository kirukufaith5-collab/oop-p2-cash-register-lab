class CashRegister:
    def __init__(self, discount=0):
        # We assign via the setter to automatically run the 0-100 validation
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # --- Properties ---
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure it is an integer
        try:
            value = int(value)
        except (ValueError, TypeError):
            print("Not valid discount")
            return

        # Ensure it is between 0 and 100 inclusive
        if 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # --- Methods ---
    def add_item(self, item, price, quantity):
        line_total = price * quantity
        self.total += line_total
        self.items.append(item)
        
        # Save transaction history as an object (dictionary)
        transaction_record = {
            "item": item,
            "price": price,
            "quantity": quantity,
            "line_total": line_total
        }
        self.previous_transactions.append(transaction_record)
        print(f"Added {quantity}x {item} for ${line_total:.2f}")

    def apply_discount(self):
        # Calculate the discount multiplier (e.g., 20% discount means paying 80%)
        multiplier = (100 - self.discount) / 100
        self.total = self.total * multiplier
        print(f"Applied {self.discount}% discount to total. New total: ${self.total:.2f}")

    def void_last_transaction(self):
        # If no transactions in array, print warning
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Remove the last item of previous_transaction from array
        last_tx = self.previous_transactions.pop()
        
        # Ensure price reflects correctly (deduct from total)
        self.total -= last_tx["line_total"]
        
        # Ensure items reflects correctly (remove from list)
        if last_tx["item"] in self.items:
            self.items.remove(last_tx["item"])
            
        print(f"Voided last transaction: {last_tx['quantity']}x {last_tx['item']}.")


# --- Allow for user to input ---
if __name__ == "__main__":
    user_input = input("Enter standard discount percentage (Press Enter for 0): ").strip()
    
    # If no input, initialize as 0
    if user_input == "":
        register = CashRegister()
    else:
        register = CashRegister(user_input)
        
    # Quick Test Run
    register.add_item("Laptop", 1000, 1)
    register.add_item("Mouse", 50, 2) # Total is 1100
    register.void_last_transaction()    # Removes Mouse, total back to 1000
    register.apply_discount()           # Applies discount to remaining total
