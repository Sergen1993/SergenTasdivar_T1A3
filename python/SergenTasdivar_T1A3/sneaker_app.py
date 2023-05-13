import sys
from tabulate import tabulate
from termcolor import colored
from products import products

cart = []

def display_menu():
    print(colored("MENU:", 'blue'))
    print("1. View products")
    print("2. Add product to cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Quit")

def view_products():
    headers = ['ID', 'Product', 'Price']
    table = []
    for i, product in enumerate(products, start=1):
        table.append([i, product['name'], product['price']])
    print(colored(tabulate(table, headers, tablefmt="grid"), 'blue'))

def add_to_cart():
    view_products()
    while True:
        try:
            choice = int(input("Enter the ID of the product to add to cart (0 to cancel): "))
            if choice == 0:
                break
            elif choice < 1 or choice > len(products):
                raise ValueError
            product = products[choice - 1]
            quantity = int(input("Enter the quantity: "))
            if quantity <= 0:
                raise ValueError
            product['quantity'] = quantity
            cart.append(product)
            print(colored(f"Added '{product['name']}' to cart.", 'green'))
            break
        except ValueError:
            print(colored("Invalid input! Please enter a valid product ID and quantity.", 'red'))

def view_cart():
    headers = ['ID', 'Product', 'Price', 'Quantity']
    table = []
    total_price = 0
    for i, product in enumerate(cart, start=1):
        table.append([i, product['name'], product['price'], product['quantity']])
        total_price += product['price'] * product['quantity']
    print(colored(tabulate(table, headers, tablefmt="grid"), 'blue'))
    print(colored(f"Total price: ${total_price}", 'green'))

def checkout():
    view_cart()
    confirm = input("Confirm checkout? (y/n): ")
    if confirm.lower() == 'y':
        print(colored("Thank you for your purchase!", 'green'))
        sys.exit()
    else:
        print(colored("Checkout canceled.", 'red'))

def quit_program():
    print(colored("Goodbye!", 'green'))
    sys.exit()

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            quit_program()
        else:
            print(colored("Invalid input! Please enter a valid menu option.", 'red'))

if __name__ == '__main__':
    main()
