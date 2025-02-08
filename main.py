from products import Product
from store import Store

def main():
    # Step 1: 
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=50),
        Product("Google Pixel 7", price=500, quantity=25)
    ]

    # Step 2: 
    best_buy = Store(product_list)

    # Step 3: 
    start(best_buy)

def start(store_obj):
    """
    Provides an interactive menu for the user to interact with the store.
    """
    while True:
        print("\n==== Best Buy Store ====")
        print("1. List all products")
        print("2. Show total stock quantity")
        print("3. Make an order")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # List all available products
            print("\nAvailable Products:")
            for product in store_obj.get_all_products():
                print(product)

        elif choice == "2":
            # Show total quantity of all products in the store
            print(f"\nTotal stock quantity: {store_obj.get_total_quantity()}")

        elif choice == "3":
            # Make an order by selecting a product and quantity
            try:
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))

                # Find the product by name
                product = next((p for p in store_obj.products if p.name == product_name), None)
                
                if product:
                    total_cost = store_obj.order([(product, quantity)])
                    print(f"✅ Order successful! Total cost: ${total_cost:.2f}")
                else:
                    print("❌ Product not found! Try again.")

            except ValueError as e:
                print(f"⚠ Error: {e}")

        elif choice == "4":
            # Exit the program
            print("Exiting... Thank you for shopping at Best Buy!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
