def calculate_movie_ticket():
    print("\n----- Welcome to Movie Theater Billing System -----")
    
    # Get input from user
    is_birthday = input("Is it your birthday? (yes/no): ").lower()
    has_credit_card = input("Do you have a credit card? (yes/no): ").lower()
    age = int(input("Enter your age: "))
    is_loyal_customer = input("Are you a loyal customer? (yes/no): ").lower()

    # Initialize ticket price
    ticket_price = 200  # Base ticket price

    # Apply age-based discounts
    if age <= 12:  # Children discount (12 and under)
        ticket_price *= 0.7  # 30% off
        print("Children discount applied (30% off).")
    elif 13 <= age <= 19:  # Teenager discount
        ticket_price *= 0.9  # 10% off
        print("Teenager discount applied (10% off).")
    elif 60 <= age:  # Senior citizen discount (60 and above)
        ticket_price *= 0.8  # 20% off
        print("Senior citizen discount applied (20% off).")
    else:  # Adults (20 to 59)
        ticket_price *= 0.95  # 5% off
        print("Adult discount applied (5% off).")

    # Apply additional discounts
    if is_birthday == "yes":
        ticket_price *= 0.85  # 15% birthday discount
        print("Birthday discount applied (15% off).")

    if has_credit_card == "yes":
        ticket_price *= 0.95  # 5% credit card discount
        print("Credit card discount applied (5% off).")

    if is_loyal_customer == "yes":
        ticket_price *= 0.9  # 10% loyal customer discount
        print("Loyal customer discount applied (10% off).")

    # Ask for additional items
    add_ons = 0
    menu = {
        "popcorn": 100,
        "coke": 50,
        "chips": 30,
        "ice cream": 70,
        "fries": 80
    }

    print("\n----- Menu for Add-ons -----")
    for item, price in menu.items():
        print(f"{item.title()}: Rs. {price}")

    for item, price in menu.items():
        choice = input(f"Would you like to add {item}? (yes/no): ").lower()
        if choice == "yes":
            add_ons += price

    # Parking charges
    parking_charge = 0
    need_parking = input("\nDo you need parking? (yes/no): ").lower()
    if need_parking == "yes":
        vehicle_type = input("Enter vehicle type (bike/car): ").lower()
        if vehicle_type == "bike":
            parking_charge = 20  # Rs. 20 for bikes
        elif vehicle_type == "car":
            parking_charge = 50  # Rs. 50 for cars
        else:
            print("Invalid vehicle type! No parking charges applied.")

    # Smoking fine
    smoking_fine = 0
    caught_smoking = input("\nWere you caught smoking inside the premises? (yes/no): ").lower()
    if caught_smoking == "yes":
        smoking_fine = 500  # Rs. 500 fine for smoking
        print("Smoking fine applied (Rs. 500).")

    # GST (Goods and Services Tax)
    gst_rate = 0.18
    gst_amount = (ticket_price + add_ons + parking_charge) * gst_rate

    # Loyalty points
    loyalty_points = 0
    if is_loyal_customer == "yes":
        loyalty_points = int((ticket_price + add_ons) // 10)
        print(f"Loyalty points earned: {loyalty_points}")

    # Calculate final bill
    total_bill = ticket_price + add_ons + parking_charge + smoking_fine + gst_amount

    # Print the bill details
    print("\n----- Final Movie Ticket Bill Details -----")
    print(f"Base ticket price after discounts: Rs. {ticket_price:.2f}")
    print(f"Additional items: Rs. {add_ons:.2f}")
    print(f"Parking charges: Rs. {parking_charge:.2f}")
    print(f"Smoking fine: Rs. {smoking_fine:.2f}")
    print(f"GST (18%): Rs. {gst_amount:.2f}")
    print(f"Total Amount: Rs. {total_bill:.2f}")

    if is_loyal_customer == "yes":
        print(f"Loyalty points earned: {loyalty_points}")


# Run the function
calculate_movie_ticket()
