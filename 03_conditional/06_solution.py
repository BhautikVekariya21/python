def select_transportation_mode(distance):
    """
    Suggest a transportation mode based on the given distance.
    """
    if distance < 0:
        return "Invalid distance. Please enter a positive number."
    elif distance <= 1:
        return "It's less than 1 km. Walking is the best choice!"
    elif distance <= 3:
        return "It's between 1 km and 3 km. A bicycle is a great option."
    elif distance <= 5:
        return "It's between 3 km and 5 km. Consider taking an auto-rickshaw."
    elif distance <= 10:
        return "It's between 5 km and 10 km. A scooter or motorbike is a good choice."
    elif distance <= 20:
        return "It's between 10 km and 20 km. Use a car or book a cab."
    elif distance <= 50:
        return "It's between 20 km and 50 km. Public transport like buses or trains is economical."
    elif distance <= 500:
        return "It's between 50 km and 500 km. Consider booking a train or an intercity bus."
    else:
        return "For distances greater than 500 km, traveling by flight is recommended."


# Main program
print("Transportation Mode Selector")
print("-----------------------------")

while True:
    try:
        user_input = input("\nEnter the distance (in km) or type 'exit' to quit: ").lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        distance = float(user_input)
        suggestion = select_transportation_mode(distance)
        print("\nSuggested Transportation Mode:")
        print(suggestion)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
