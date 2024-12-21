def suggest_activity(weather, temperature):
    """
    Suggest an activity based on the weather and temperature.
    """
    weather = weather.lower()
    activity = ""

    if weather == "sunny":
        if temperature > 35:
            activity = "It's extremely hot! Stay indoors with air conditioning or visit a pool."
        elif 25 <= temperature <= 35:
            activity = "Perfect weather for a beach day, outdoor sports, or a barbecue."
        elif 15 <= temperature < 25:
            activity = "Great day for a walk, a picnic, or exploring a park."
        else:
            activity = "It's sunny but cool. Wear a jacket and enjoy a light outdoor activity."

    elif weather == "rainy":
        if temperature > 20:
            activity = "Enjoy the rain by visiting a café, watching movies, or dancing in the rain."
        elif 10 <= temperature <= 20:
            activity = "Rainy and cool weather is perfect for staying in with hot tea and a good book."
        else:
            activity = "It's cold and rainy. Stay warm indoors and enjoy cozy indoor activities."

    elif weather == "cloudy":
        if temperature > 20:
            activity = "Cloudy but warm! Visit a museum, go shopping, or enjoy a walk."
        elif 10 <= temperature <= 20:
            activity = "It's cool and cloudy. Great for a bike ride or a visit to the library."
        else:
            activity = "Cloudy and chilly weather. Relax indoors or do some light housework."

    elif weather == "snowy":
        if temperature < -10:
            activity = "Extreme cold! Stay indoors with warm drinks and a fireplace if possible."
        elif 0 <= temperature <= -10:
            activity = "Snowy and cold. Go skiing, build a snowman, or have a snowball fight."
        else:
            activity = "Light snow. Take a scenic walk or enjoy winter photography."

    elif weather == "windy":
        if temperature > 25:
            activity = "It's windy and warm. Fly kites, go to the beach, or enjoy windsurfing."
        elif 10 <= temperature <= 25:
            activity = "Cool and windy. Visit an indoor amusement park or go bowling."
        else:
            activity = "Cold and windy. Stay indoors or bundle up if you must go outside."

    elif weather == "stormy":
        activity = "Stay indoors and stay safe! A great time for indoor hobbies like painting, crafting, or board games."

    elif weather == "foggy":
        if temperature > 15:
            activity = "Foggy but mild. Enjoy photography or take a short, cautious walk."
        else:
            activity = "Foggy and cool. Avoid unnecessary travel and enjoy a cozy indoor day."

    elif weather == "hazy":
        if temperature > 30:
            activity = "Hazy and hot. Limit outdoor activities and stay hydrated."
        else:
            activity = "Hazy weather. Stay indoors to avoid breathing issues and do light exercises."

    elif weather == "drizzle":
        activity = "Light drizzle outside. Wear a raincoat and take a refreshing walk, or enjoy the sound of rain indoors."

    elif weather == "frosty":
        activity = "Frosty conditions. Stay warm indoors, or go outside for frost photography and short walks."

    elif weather == "humid":
        if temperature > 30:
            activity = "It's hot and humid. Stay indoors or visit a swimming pool."
        else:
            activity = "Mildly humid weather. Go for a relaxing evening walk or visit a park."

    else:
        activity = "Weather condition not recognized. Be prepared and enjoy your day!"

    return activity


# Main program
print("Enhanced Weather Activity Suggestion")
print("-------------------------------------")

while True:
    weather = input("\nEnter the weather condition (e.g., sunny, rainy, cloudy, snowy, windy, stormy, foggy, hazy, drizzle, frosty, humid): ")
    if weather.lower() == "exit":
        print("Goodbye!")
        break

    try:
        temperature = float(input("Enter the temperature (in °C): "))
    except ValueError:
        print("Invalid temperature. Please enter a number.")
        continue

    suggestion = suggest_activity(weather, temperature)
    print("\nSuggested Activity:")
    print(suggestion)
