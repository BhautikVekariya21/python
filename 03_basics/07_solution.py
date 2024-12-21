def coffee_order():
    """
    Function to take coffee customization order and calculate the bill with various Starbucks coffee options.
    """
    # Define base prices for coffee types
    coffee_prices = {
        "Caffee Americano": 100,
        "Cappuccino": 120,
        "Caffee Latte": 150,
        "Caramel Macchiato": 180,
        "Iced Latte": 130,
        "Flat White": 160,
        "Mocha": 170,
        "Espresso": 90,
        "Macchiato": 140,
        "Nitro Cold Brew": 200,
        "Pumpkin Spice Latte": 190,
        "Java Chip Frappuccino": 210
    }
    
    # Define calories for coffee types
    coffee_calories = {
        "Caffee Americano": 0,
        "Cappuccino": 120,
        "Caffee Latte": 190,
        "Caramel Macchiato": 100,
        "Iced Latte": 150,
        "Flat White": 170,
        "Mocha": 200,
        "Espresso": 5,
        "Macchiato": 100,
        "Nitro Cold Brew": 10,
        "Pumpkin Spice Latte": 220,
        "Java Chip Frappuccino": 300
    }
    
    # Size options and price adjustments
    size_prices = {
        "small": 0,
        "medium": 20,
        "large": 40
    }
    
    # Milk customization options
    milk_options = {
        "Whole Milk": 0,
        "Skim Milk": 10,
        "Soy Milk": 15,
        "Almond Milk": 20,
        "Oat Milk": 25
    }
    
    # Syrup customization options
    syrup_options = {
        "Vanilla Syrup": 15,
        "Caramel Syrup": 15,
        "Hazelnut Syrup": 15,
        "Pumpkin Spice Syrup": 20,
        "Chocolate Syrup": 20
    }
    
    print("Welcome to Coffee Customization!\n")
    
    # Choose coffee type
    print("Available Coffee Types:")
    for coffee in coffee_prices:
        print(coffee)
    coffee_type = input("\nEnter your choice of coffee: ").strip().title()
    
    if coffee_type not in coffee_prices:
        print("Invalid coffee type selected.")
        return
    
    # Choose size
    print("\nAvailable Sizes: small, medium, large")
    size = input("Enter your preferred size: ").strip().lower()
    
    if size not in size_prices:
        print("Invalid size selected.")
        return
    
    # Choose milk option
    print("\nAvailable Milk Options:")
    for milk in milk_options:
        print(milk)
    milk_choice = input("Choose your milk option: ").strip().title()
    
    if milk_choice not in milk_options:
        print("Invalid milk option selected.")
        return
    
    # Choose syrup option
    print("\nAvailable Syrup Options:")
    for syrup in syrup_options:
        print(syrup)
    syrup_choice = input("Choose your syrup option: ").strip().title()
    
    if syrup_choice not in syrup_options:
        print("Invalid syrup option selected.")
        return
    
    # Choose calorie customization
    print("\nCalorie Customization Options:")
    print("0 cal, 120 cal, 190 cal, 100 cal (depending on the coffee type)")
    calorie_customization = int(input("Enter the calorie option: "))
    
    if calorie_customization not in [0, 120, 190, 100]:
        print("Invalid calorie option selected.")
        return
    
    # Calculate price based on coffee type, size, milk, and syrup
    base_price = coffee_prices[coffee_type]
    size_price = size_prices[size]
    milk_price = milk_options[milk_choice]
    syrup_price = syrup_options[syrup_choice]
    
    total_price = base_price + size_price + milk_price + syrup_price
    
    # Display coffee details and total price
    print("\n----- Your Coffee Order -----")
    print(f"Coffee Type: {coffee_type}")
    print(f"Size: {size.capitalize()}")
    print(f"Milk: {milk_choice}")
    print(f"Syrup: {syrup_choice}")
    print(f"Calories: {calorie_customization} cal")
    print(f"Price: Rs. {total_price}")
    
    # Final confirmation of the bill
    confirm = input("\nWould you like to add another coffee? (yes/no): ").strip().lower()
    if confirm == "yes":
        coffee_order()  # Recursively call to add more coffees
    else:
        print(f"\nTotal Bill: Rs. {total_price}")
        print("Thank you for your order!")


# Main program
coffee_order()
