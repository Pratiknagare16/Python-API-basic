import requests



def get_user_info():
    print("\n=== User Information Lookup ===")

    user_id = input("Enter user ID (1-10): ").strip()

    
    if not user_id.isdigit():
        print(" Please enter numbers only.")
        return

    if int(user_id) < 1 or int(user_id) > 10:
        print(" User ID must be between 1 and 10.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print("Name   :", data["name"])
        print("Email  :", data["email"])
        print("Phone  :", data["phone"])
        print("Website:", data["website"])
    else:
        print("User not found.")



def search_posts():
    print("\n=== Post Search ===")

    user_id = input("Enter user ID: ").strip()

    
    if not user_id.isdigit():
        print(" Please enter numbers only.")
        return

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, params={"userId": user_id})
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User {user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found.")



def get_crypto_price():
    print("\n=== Crypto Price ===")
    print("Available: btc-bitcoin, eth-ethereum, doge-dogecoin")

    coin_id = input("Enter coin id: ").lower().strip()

    if coin_id == "":
        print(" Coin name cannot be empty.")
        return

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n{data['name']} ({data['symbol']})")
        print("Price:", f"${data['quotes']['USD']['price']:,.2f}")
        print("24h Change:", f"{data['quotes']['USD']['percent_change_24h']}%")
    else:
        print(" Coin not found.")



def get_weather():
    print("\n=== Weather Checker ===")

    city = input("Enter city name: ").strip()

    if city == "":
        print(" City cannot be empty.")
        return

    
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_response = requests.get(geo_url, params={"name": city, "count": 1})
    geo_data = geo_response.json()

    if "results" not in geo_data:
        print(" City not found.")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]


    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_response = requests.get(weather_url, params={
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    })

    weather = weather_response.json()["current_weather"]

    print(f"\n Weather in {city.title()}")
    print(" Temperature:", weather["temperature"], "°C")
    print(" Wind Speed :", weather["windspeed"], "km/h")



def search_todos():
    print("\n=== Todo Search ===")
    print("Type 'true' for completed tasks")
    print("Type 'false' for incomplete tasks")

    status = input("Enter status (true / false): ").lower().strip()

    if status not in ["true", "false"]:
        print(" Please enter only true or false.")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"completed": status})
    todos = response.json()

    print(f"\nFound {len(todos)} tasks with completed = {status}\n")
    for i, todo in enumerate(todos[:15], 1):
        print(f"{i}. {todo['title']}")



def main():
    while True:
        print("\n==============================")
        print("       API DEMO APP")
        print("==============================")
        print("1. User Info")
        print("2. User Posts")
        print("3. Crypto Price")
        print("4. Weather")
        print("5. Todos (Completed / Pending)")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_weather()
        elif choice == "5":
            search_todos()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print(" Invalid choice.")


if __name__ == "__main__":
    main()
