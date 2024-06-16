# pos_sytem_program
This POS (Point of Sale) system program is designed for calculating sales, entering and storing product information, customer information, and calculating purchase invoices
Below is a detailed description of the program's functionality and its components:

Main Features:
Product Management:

Add Product: Staff can input and save product information, including product code, name, and price. Each product is stored in a dictionary for easy access and retrieval.
Product Storage: The products are stored in a dictionary where the keys are product codes, and the values are instances of the Product class containing the product's details.
Customer Management:

Add Customer: Staff can input and save customer information, including customer ID, name, and phone number. Each customer is stored in a dictionary for easy access and retrieval.
Customer Storage: The customers are stored in a dictionary where the keys are customer IDs, and the values are instances of the Customer class containing the customer's details.
Sales Calculation:

Order Calculation: The program allows staff to calculate the total amount of a customer's order. Staff input the customer's ID and the product codes with the quantities purchased. The program then calculates the total cost by summing the price of each product multiplied by the quantity.
Invoice Generation: After the order is calculated, the program generates a summary of the invoice, including the total amount due.
Components of the Program:
Product Class:

Stores information about each product, including its code, name, and price.
python
Sao chép mã
class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
Customer Class:

Stores information about each customer, including their ID, name, and phone number.
python
Sao chép mã
class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
Store Class:

Manages the overall functionality of the POS system, including adding products, adding customers, and calculating orders.
Contains methods to add products, add customers, and calculate orders.
Uses dictionaries to store products and customers for quick access and management.
python
Sao chép mã
class Store:
    def __init__(self):
        self.products = {}
        self.customers = {}

    def add_product(self):
        product_code = input("Enter product code: ").upper()
        if product_code in self.products:
            print("Product already exists. Please enter a different code.")
            return
        name = input("Enter product name: ")
        try:
            price = float(input("Enter product price: "))
            if price <= 0:
                print("Price must be greater than 0. Please re-enter.")
                return
        except ValueError:
            print("Price must be a number. Please re-enter.")
            return
        product = Product(product_code, name, price)
        self.products[product_code] = product
        print(f"Added product: {name} (Code: {product_code}, Price: {price} VND)")

    def add_customer(self):
        customer_id = input("Enter customer ID: ").upper()
        if customer_id in self.customers:
            print("Customer already exists. Please enter a different ID.")
            return
        name = input("Enter customer name: ")
        phone = input("Enter customer phone number: ")
        customer = Customer(customer_id, name, phone)
        self.customers[customer_id] = customer
        print(f"Added customer: {name} (ID: {customer_id}, Phone: {phone})")

    def calculate_order(self):
        total_amount = 0
        customer_id = input("Enter customer ID: ").upper()
        if customer_id not in self.customers:
            print("Customer does not exist. Please add the customer first.")
            return
        customer = self.customers[customer_id]
        print(f"Customer: {customer.name} (ID: {customer_id}, Phone: {customer.phone})")
        
        while True:
            product_code = input("Enter product code (enter 'q' to quit): ").upper()
            if product_code == 'Q':
                break
            if product_code in self.products:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0. Please re-enter.")
                        continue
                    product = self.products[product_code]
                    item_total = product.price * quantity
                    total_amount += item_total
                    print(f"{quantity} x {product.name} at {product.price} VND each. Total: {item_total} VND")
                except ValueError:
                    print("Quantity must be an integer. Please re-enter.")
            else:
                print("Invalid product code. Please re-enter.")
        
        print(f"Total order amount for {customer.name}: {total_amount} VND")
Main Function:

Runs the main loop of the program, allowing staff to choose between adding products, adding customers, calculating orders, or exiting the program.
python
Sao chép mã
def main():
    store = Store()
    while True:
        print("\nSales Management Program")
        print("1. Add product")
        print("2. Add customer")
        print("3. Calculate order")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            store.add_product()
        elif choice == '2':
            store.add_customer()
        elif choice == '3':
            store.calculate_order()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
Summary
This POS system program is an efficient tool for managing sales in a clothing store. It allows staff to:

Enter and store product information.
Enter and store customer information.
Calculate the total amount for customer orders.
The use of classes makes the program modular and easy to maintain, ensuring that each part of the functionality (product management, customer management, order calculation) is encapsulated within its respective class.
