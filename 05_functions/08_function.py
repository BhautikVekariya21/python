def print_person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
print_person_details(name="Anamika", age=30, city="New York")

def display_info(*args, **kwargs):
    print("Positional Arguments (*args):", args)
    print("Keyword Arguments (**kwargs):", kwargs)

# Example usage:
display_info(1, 2, 3, name="Sharma", age=25)

def greet_user(**kwargs):
    greeting = "Hello"
    if 'name' in kwargs:
        greeting += f", {kwargs['name']}!"
    if 'time_of_day' in kwargs:
        greeting += f" Good {kwargs['time_of_day']}!"
    return greeting

# Example usage:
greeting = greet_user(name="Vin", time_of_day="Morning")
print(greeting)

def apply_discount(**kwargs):
    price = kwargs.get("price", 0)
    discount_type = kwargs.get("discount_type", "flat")
    
    if discount_type == "flat":
        discount = kwargs.get("flat_discount", 0)
    elif discount_type == "percentage":
        discount = (kwargs.get("percentage_discount", 0) / 100) * price
    else:
        discount = 0

    final_price = price - discount
    return final_price

# Example usage:
final_price = apply_discount(price=100, discount_type="percentage", percentage_discount=20)
print(f"Final Price after discount: {final_price}")
