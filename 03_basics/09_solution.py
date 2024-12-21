def is_leap_year(year):
    """
    Function to check if a given year is a leap year.
    """
    # Leap year rules:
    # 1. A year is a leap year if it is divisible by 4.
    # 2. However, if it is divisible by 100, it is not a leap year, unless...
    # 3. It is also divisible by 400, in which case it is a leap year.
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Main program
def main():
    year = int(input("Enter a year to check if it's a leap year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
