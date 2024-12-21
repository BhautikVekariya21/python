
# Function to calculate electricity bill based on units consumed
def calculate_electricity_bill():
    # Get input from user
    units = float(input("Enter number of units consumed: "))
    
    # Initialize bill amount
    bill = 0
    
    # Calculate bill according to criteria
    if units <= 100:
        bill = 0
    elif units <= 200:
        bill = (units - 100) * 5
    else:
        bill = (100 * 5) + ((units - 200) * 10)
        
    # Print the total bill amount
    print(f"Total Bill Amount: Rs. {bill}")

# Call the function
calculate_electricity_bill()

