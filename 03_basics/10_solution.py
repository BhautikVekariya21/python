def recommend_food(pet_type, age, size, activity_level):
    """
    Function to recommend pet food based on the pet type, age, size, and activity level.
    """
    if pet_type.lower() == "dog":
        if age.lower() == "puppy":
            if size.lower() == "small":
                return "Recommended food: Pedigree Small Breed Puppy Food (High Protein, Small Kibbles)"
            elif size.lower() == "medium":
                return "Recommended food: Pedigree Medium Breed Puppy Food (Balanced Nutrition)"
            elif size.lower() == "large":
                return "Recommended food: Pedigree Large Breed Puppy Food (Supports Bone Growth)"
        elif age.lower() == "adult":
            if activity_level.lower() == "high":
                return "Recommended food: Pedigree Adult High Energy Dog Food (Protein-rich for Active Dogs)"
            else:
                return "Recommended food: Pedigree Adult Dog Food (Balanced Diet for Regular Dogs)"
        elif age.lower() == "senior":
            return "Recommended food: Pedigree Senior Dog Food (Supports Joint Health and Mobility)"
        else:
            return "Invalid age for dog. Please enter puppy, adult, or senior."
    
    elif pet_type.lower() == "cat":
        if age.lower() == "kitten":
            return "Recommended food: Whiskas Kitten Food (High Protein for Growth and Development)"
        elif age.lower() == "adult":
            if activity_level.lower() == "high":
                return "Recommended food: Whiskas Adult High Protein Cat Food (Supports Active Cats)"
            else:
                return "Recommended food: Whiskas Adult Cat Food (Balanced Nutrition for Regular Cats)"
        elif age.lower() == "senior":
            return "Recommended food: Whiskas Senior Cat Food (Supports Kidney and Joint Health)"
        else:
            return "Invalid age for cat. Please enter kitten, adult, or senior."
    
    elif pet_type.lower() == "fish":
        if size.lower() == "small":
            return "Recommended food: TetraMin Small Fish Pellets (Suitable for Goldfish, Guppies)"
        elif size.lower() == "medium":
            return "Recommended food: TetraMin Medium Fish Pellets (Suitable for Betta Fish, Tetras)"
        elif size.lower() == "large":
            return "Recommended food: TetraMin Large Fish Flakes (Suitable for Cichlids, Large Aquarium Fish)"
        else:
            return "Invalid size for fish. Please enter small, medium, or large."
    
    elif pet_type.lower() == "rabbit":
        if size.lower() == "small":
            return "Recommended food: Oxbow Essentials Rabbit Food (High Fiber, Small Pellets)"
        elif size.lower() == "medium":
            return "Recommended food: Oxbow Animal Health Garden Select Rabbit Food (Nutritious for Medium-sized Rabbits)"
        elif size.lower() == "large":
            return "Recommended food: Oxbow Garden Select Rabbit Food (High-Quality Ingredients for Large Rabbits)"
        else:
            return "Invalid size for rabbit. Please enter small, medium, or large."
    
    elif pet_type.lower() == "hamster":
        if size.lower() == "small":
            return "Recommended food: Kaytee Forti-Diet Pro Health Hamster Food (For Small Hamsters)"
        elif size.lower() == "medium":
            return "Recommended food: Kaytee Forti-Diet Pro Health Hamster Food (For Medium-sized Hamsters)"
        else:
            return "Invalid size for hamster. Please enter small or medium."
    
    elif pet_type.lower() == "buffalo":
        if size.lower() == "small":
            return "Recommended food: Buffalo Starter Feed (Nutrient-rich for Calves)"
        elif size.lower() == "medium":
            return "Recommended food: Buffalo Growth Feed (Supports Growth and Weight Gain)"
        elif size.lower() == "large":
            return "Recommended food: Buffalo Finisher Feed (For Mature Buffaloes, High Energy)"
        else:
            return "Invalid size for buffalo. Please enter small, medium, or large."
    
    elif pet_type.lower() == "cow":
        if size.lower() == "small":
            return "Recommended food: Cow Starter Feed (Rich in Protein for Calves)"
        elif size.lower() == "medium":
            return "Recommended food: Cow Growth Feed (For Growing Cows, High in Nutrients)"
        elif size.lower() == "large":
            return "Recommended food: Cow Finisher Feed (For Mature Cows, Balanced for Milk Production)"
        else:
            return "Invalid size for cow. Please enter small, medium, or large."
    
    else:
        return "Sorry, we don't have food recommendations for this pet type. Please enter dog, cat, fish, rabbit, hamster, buffalo, or cow."

# Main program
def main():
    print("Welcome to the Pet Food Recommendation System!")
    pet_type = input("Enter your pet type (dog, cat, fish, rabbit, hamster, buffalo, cow): ").strip()
    age = input("Enter your pet's age (puppy/kitten/adult/senior): ").strip()
    
    if pet_type.lower() == "dog" or pet_type.lower() == "cat":
        size = input("Enter your pet's size (small/medium/large): ").strip()
    else:
        size = input("Enter your pet's size (small/medium/large): ").strip()

    if pet_type.lower() == "dog" or pet_type.lower() == "cat":
        activity_level = input("Enter your pet's activity level (high/low): ").strip()
    else:
        activity_level = "low"  # Default for fish, rabbit, hamster, buffalo, cow as activity level isn't considered

    food_recommendation = recommend_food(pet_type, age, size, activity_level)
    print(food_recommendation)

if __name__ == "__main__":
    main()
