import random

def calculate_discount():
    total_price = 0
    print("Enter the price of each item. Type '0' when done.")
    
    while True:
        try:
            price = float(input("Enter price: "))
            if price == 0:
                break
            elif price < 0:
                print("Price cannot be negative. Try again.")
                continue
            total_price += price
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if total_price == 0:
        print("No items entered. No discount applied.")
        return
    
    if 0 <= total_price <= 50:
        discount_rate = 0.10
    elif 51 <= total_price <= 75:
        discount_rate = 0.15
    else:
        discount_rate = 0.20
    
    discount = total_price * discount_rate
    new_total = total_price - discount
    
    print(f"Original Total: ${total_price:.2f}")
    print(f"Discount ({int(discount_rate * 100)}%): -${discount:.2f}")
    print(f"New Total: ${new_total:.2f}")

def random_number_generator():
    random_number = random.randint(1, 100)
    print(f"Your random number is: {random_number}")

while True:
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    print("Welcome! What can I help you with today?")
    
    while True:
        print("\nOptions:")
        print("1. Calculate Sales Discount")
        print("2. Generate a Random Number")
        print("3. Exit the Program")
        
        choice = input("Please select an option (1, 2, or 3): ")
        
        if choice == '1':
            calculate_discount()
        elif choice == '2':
            random_number_generator()
        elif choice == '3':
            print("Thank you for using the program. Goodbye!")
            exit() 
        else:
            print("Invalid choice. Please try again.")
            continue
        
        more_help = input("\nDo you need help with anything else? (yes or no): ").strip().lower()
        if more_help != 'yes':
            print("Thank you for using the program. Goodbye!")
            exit()
