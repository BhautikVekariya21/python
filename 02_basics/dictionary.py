
# Creating a dictionary of countries and capitals
country_capitals = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin"
}

# Performing dictionary methods
print("Original dictionary:", country_capitals)
print("\nKeys:", country_capitals.keys())
print("Values:", country_capitals.values())
print("Items:", country_capitals.items())

# Adding new key-value pair
country_capitals["Japan"] = "Tokyo"

# Updating value
country_capitals["USA"] = "Washington D.C."

# Removing item
del country_capitals["France"]

# Creating nested dictionary with additional info
country_info = {
    "India": {
        "capital": "New Delhi",
        "population": "1.4 billion",
        "languages": ["Hindi", "English"]
    },
    "USA": {
        "capital": "Washington D.C.",
        "population": "331 million",
        "languages": ["English"]
    }
}

# Accessing nested dictionary
print("\nIndia's population:", country_info["India"]["population"])

# Generating KeyError by trying to access non-existent key
try:
    print(country_capitals["Spain"])
except KeyError as e:
    print("\nError occurred:", e)

# Generating TypeError by incorrect method usage
# try:
#     country_capitals.update("Italy")  # Should pass key-value pair, not just string
# except TypeError as e:
#     print("TypeError occurred:", e)

# Get length of dictionary
print("Length of dictionary:", len(country_capitals))

# Check if key exists
print("Is USA in dictionary?", "USA" in country_capitals)
print("Is Spain in dictionary?", "Spain" in country_capitals)

# Get value with default if key doesn't exist
print("Capital of Spain:", country_capitals.get("Spain", "Not found"))

# Copy dictionary
capitals_copy = country_capitals.copy()
print("Copied dictionary:", capitals_copy)

# Create dictionary from sequences
countries = ["China", "Brazil"]
capitals = ["Beijing", "Brasilia"] 
new_dict = dict(zip(countries, capitals))
print("New dictionary from sequences:", new_dict)

# Update dictionary with another dictionary
country_capitals.update(new_dict)
print("Updated dictionary:", country_capitals)

# Pop item with default value
removed_capital = country_capitals.pop("Brazil", "Not found")
print("Removed capital:", removed_capital)

# Pop last inserted item
last_item = country_capitals.popitem()
print("Last removed item:", last_item)

# Create dictionary with same keys and None values
new_dict = dict.fromkeys(countries)

# Set default value if key doesn't exist
country_capitals.setdefault("Spain", "Madrid")
print("After setdefault:", country_capitals)

# Clear the dictionary
country_capitals.clear()
print("After clearing:", country_capitals)

# Create a dictionary using dict() constructor
fruits_prices = dict(apple=2.5, banana=1.5, orange=3.0, mango=4.0)

# Display original dictionary
print("Original dictionary:", fruits_prices)

# Get all keys and values
print("\nKeys:", fruits_prices.keys())
print("Values:", fruits_prices.values()) 
print("Items:", fruits_prices.items())

# Add new item
fruits_prices["grape"] = 3.5

# Update existing value
fruits_prices["apple"] = 2.75

# Remove item
del fruits_prices["orange"]

# Get length
print("\nNumber of items:", len(fruits_prices))

# Check if key exists
print("Is apple in dictionary?", "apple" in fruits_prices)
print("Is orange in dictionary?", "orange" in fruits_prices)

# Get value with default
print("Price of kiwi:", fruits_prices.get("kiwi", "Not available"))

# Create copy
fruits_copy = fruits_prices.copy()

# Create from sequences
fruits = ["pear", "plum"]
prices = [2.0, 1.75]
new_fruits = dict(zip(fruits, prices))

# Update with another dictionary
fruits_prices.update(new_fruits)

# Pop item
removed_price = fruits_prices.pop("plum")
print("\nRemoved price:", removed_price)

# Pop last item
last_item = fruits_prices.popitem()
print("Last removed item:", last_item)

# Set default value
fruits_prices.setdefault("kiwi", 5.0)

# Clear dictionary
fruits_prices.clear()
print("\nAfter clearing:", fruits_prices)