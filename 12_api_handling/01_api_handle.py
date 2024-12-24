import requests

# Fetch random user data from FreeAPI
def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data.get("success") and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")

# Fetch a random joke
def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    else:
        raise Exception("Failed to fetch a random joke")

# Fetch weather information using OpenWeatherMap API
def fetch_weather(city):
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The weather in {city} is {temp}°C with {description}."
    else:
        raise Exception(f"Failed to fetch weather data for {city}")

# Fetch current cryptocurrency price
def fetch_crypto_price(crypto_symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data[crypto_symbol]["usd"]
        return f"The current price of {crypto_symbol.capitalize()} is ${price:.2f}."
    else:
        raise Exception(f"Failed to fetch price for {crypto_symbol}")

# Fetch a random trivia question
def fetch_random_trivia():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        return question, correct_answer
    else:
        raise Exception("Failed to fetch trivia question")

# Fetch a random health tip
def fetch_health_tip():
    url = "https://api.api-ninjas.com/v1/healthtips"
    headers = {"X-Api-Key": "your_api_ninjas_key"}  # Replace with your API key
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if len(data) > 0:
                return data[0]["tip"]
            else:
                raise Exception("No health tips available.")
        except ValueError:
            raise Exception("Invalid JSON response.")
    elif response.status_code == 401:
        raise Exception("Unauthorized: Invalid API key.")
    elif response.status_code == 403:
        raise Exception("Forbidden: API access is restricted.")
    elif response.status_code == 429:
        raise Exception("Too Many Requests: Rate limit exceeded.")
    else:
        raise Exception(f"Unexpected error: {response.status_code} - {response.text}")


# Main function to integrate functionalities
def main():
    while True:
        print("\nDiverse Functionalities App")
        print("-" * 50)
        print("1. Fetch Random User")
        print("2. Get a Random Joke")
        print("3. Get Weather Information")
        print("4. Get Cryptocurrency Price")
        print("5. Get a Random Trivia Question")
        print("6. Get a Random Health Tip")
        print("7. Exit")
        print("-" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                username, country = fetch_random_user_freeapi()
                print(f"\nUsername: {username}\nCountry: {country}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '2':
            try:
                joke = fetch_random_joke()
                print(f"\nHere's a joke for you:\n{joke}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '3':
            city = input("\nEnter the city name to get weather information: ").strip()
            try:
                weather_info = fetch_weather(city)
                print(f"\n{weather_info}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '4':
            crypto_symbol = input("\nEnter the cryptocurrency symbol (e.g., bitcoin, ethereum): ").strip().lower()
            try:
                crypto_price = fetch_crypto_price(crypto_symbol)
                print(f"\n{crypto_price}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '5':
            try:
                question, correct_answer = fetch_random_trivia()
                print(f"\nTrivia Question: {question}")
                input("Your answer: ")
                print(f"The correct answer is: {correct_answer}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '6':
            try:
                health_tip = fetch_health_tip()
                print(f"\nHealth Tip: {health_tip}")
            except Exception as e:
                print(f"Error: {str(e)}")

        elif choice == '7':
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
