class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

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
