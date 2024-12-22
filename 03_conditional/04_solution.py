def check_ripeness(fruit, characteristic):
    """
    Check the ripeness of a fruit based on its characteristics.
    """
    fruit = fruit.lower()
    characteristic = characteristic.lower()

    if fruit == "banana":
        if characteristic in ["yellow", "soft"]:
            return "The banana is ripe."
        elif characteristic in ["green", "hard"]:
            return "The banana is unripe."
        else:
            return "The banana is overripe or spoiled."

    elif fruit == "apple":
        if characteristic in ["red", "firm"]:
            return "The apple is ripe."
        elif characteristic in ["green", "hard"]:
            return "The apple is unripe."
        else:
            return "The apple is overripe or spoiled."

    elif fruit == "mango":
        if characteristic in ["yellow", "orange", "soft"]:
            return "The mango is ripe."
        elif characteristic in ["green", "hard"]:
            return "The mango is unripe."
        else:
            return "The mango is overripe or spoiled."

    elif fruit == "grape":
        if characteristic in ["purple", "black", "firm"]:
            return "The grapes are ripe."
        elif characteristic in ["green", "sour"]:
            return "The grapes are unripe."
        else:
            return "The grapes are overripe or spoiled."

    elif fruit == "strawberry":
        if characteristic in ["red", "juicy"]:
            return "The strawberry is ripe."
        elif characteristic in ["white", "hard"]:
            return "The strawberry is unripe."
        else:
            return "The strawberry is overripe or spoiled."

    elif fruit == "orange":
        if characteristic in ["orange", "juicy", "firm"]:
            return "The orange is ripe."
        elif characteristic in ["green", "hard"]:
            return "The orange is unripe."
        else:
            return "The orange is overripe or spoiled."

    elif fruit == "pineapple":
        if characteristic in ["yellow", "golden", "sweet"]:
            return "The pineapple is ripe."
        elif characteristic in ["green", "hard"]:
            return "The pineapple is unripe."
        else:
            return "The pineapple is overripe or spoiled."

    elif fruit == "watermelon":
        if characteristic in ["dark green", "hollow sound"]:
            return "The watermelon is ripe."
        elif characteristic in ["light green", "dull sound"]:
            return "The watermelon is unripe."
        else:
            return "The watermelon is overripe or spoiled."

    elif fruit == "peach":
        if characteristic in ["pink", "soft", "fragrant"]:
            return "The peach is ripe."
        elif characteristic in ["green", "hard"]:
            return "The peach is unripe."
        else:
            return "The peach is overripe or spoiled."

    elif fruit == "kiwi":
        if characteristic in ["brown", "slightly soft"]:
            return "The kiwi is ripe."
        elif characteristic in ["green", "hard"]:
            return "The kiwi is unripe."
        else:
            return "The kiwi is overripe or spoiled."

    elif fruit == "pear":
        if characteristic in ["yellow", "soft"]:
            return "The pear is ripe."
        elif characteristic in ["green", "hard"]:
            return "The pear is unripe."
        else:
            return "The pear is overripe or spoiled."

    elif fruit == "cherry":
        if characteristic in ["red", "firm"]:
            return "The cherry is ripe."
        elif characteristic in ["yellow", "sour"]:
            return "The cherry is unripe."
        else:
            return "The cherry is overripe or spoiled."

    else:
        return "Sorry, I don't have ripeness information for that fruit."


# Main program
print("Fruit Ripeness Checker")
print("-----------------------")

while True:
    fruit = input("\nEnter the name of the fruit (or type 'exit' to quit): ")
    if fruit.lower() == "exit":
        print("Goodbye!")
        break

    characteristic = input(f"Enter the characteristic of the {fruit} (e.g., color or texture): ")
    result = check_ripeness(fruit, characteristic)
    print(result)
