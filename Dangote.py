"""
Dangote Cement Inventory Management System (DCIMS)

This system is designed to manage cement stock for Dangote Cement Plc.
It allows users to add stock, sell cement, view available stock,
and automatically saves inventory data to a file.

Author: Okueso Daniel
Matric No: 24/15040
Course: SEN
"""

class DangoteInventory:
    """
    DangoteInventory class handles all inventory-related operations
    such as adding stock, selling cement, viewing stock,
    saving data, and loading data.
    """

    def __init__(self):
        """
        Constructor initializes cement stock.
        Stock value is loaded from file if available.
        """
        self.stock = 0
        self.load_stock()

    def add_stock(self, quantity):
        """
        Adds cement to the inventory.

        Parameters:
        quantity (int): Number of cement bags to add
        """
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        self.stock += quantity
        self.save_stock()
        print(f"{quantity} bags of cement added successfully.")

    def sell_cement(self, quantity):
        """
        Sells cement from the inventory.

        Parameters:
        quantity (int): Number of cement bags to sell
        """
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > self.stock:
            print("Error: Not enough cement in stock!")
        else:
            self.stock -= quantity
            self.save_stock()
            print(f"{quantity} bags of cement sold successfully.")

    def view_stock(self):
        """
        Displays the current cement stock.
        """
        print(f"Current cement stock: {self.stock} bags")

    def save_stock(self):
        """
        Saves current stock to a file for persistence.
        """
        try:
            with open("dangote_stock.txt", "w") as file:
                file.write(str(self.stock))
        except IOError:
            print("Error saving stock data.")

    def load_stock(self):
        """
        Loads stock value from file if it exists.
        """
        try:
            with open("dangote_stock.txt", "r") as file:
                self.stock = int(file.read())
        except (FileNotFoundError, ValueError):
            self.stock = 0


def main():
    """
    Main function runs the Dangote Cement Inventory Management System.
    """
    inventory = DangoteInventory()

    while True:
        print("\n========== Dangote Cement Inventory Management System ==========")
        print("1. Add Cement Stock")
        print("2. Sell Cement")
        print("3. View Current Stock")
        print("4. Exit System")
        print("==============================================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                qty = int(input("Enter quantity to add: "))
                inventory.add_stock(qty)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "2":
            try:
                qty = int(input("Enter quantity to sell: "))
                inventory.sell_cement(qty)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "3":
            inventory.view_stock()

        elif choice == "4":
            print("Thank you for using Dangote Inventory System.")
            print("System shutting down...")
            break

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
