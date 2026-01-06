
import requests
import json
import os
from datetime import datetime

# CITY COORDINATES (Exercise 1: Extended Cities)

CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "pune": (18.5204, 73.8567),
    "ahmedabad": (23.0225, 72.5714),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
}

# CRYPTO IDS

CRYPTO_IDS = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp",
}

# WEATHER (OPEN-METEO – NO API KEY)

def get_weather(city):
    city = city.lower().strip()

    if city not in CITIES:
        print(" City not supported.")
        return None

    lat, lon = CITIES[city]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(" Weather API error:", e)
        return None


def display_weather(city):
    data = get_weather(city)
    if not data:
        return

    current = data["current_weather"]

    print("\n" + "=" * 40)
    print(f"  Weather in {city.title()}")
    print("=" * 40)
    print(f"  Temperature : {current['temperature']}°C")
    print(f"  Wind Speed  : {current['windspeed']} km/h")
    print(f"  Wind Dir    : {current['winddirection']}°")
    print("=" * 40)

    save_to_file({"city": city, "weather": current}, "weather.json")


# CRYPTO PRICE (COINPAPRIKA)

def get_crypto(coin):
    coin = coin.lower().strip()
    coin_id = CRYPTO_IDS.get(coin, coin)

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def display_crypto(coin):
    data = get_crypto(coin)
    if not data:
        print(" Crypto not found.")
        return

    usd = data["quotes"]["USD"]

    print("\n" + "=" * 40)
    print(f"  {data['name']} ({data['symbol']})")
    print("=" * 40)
    print(f"  Price       : ${usd['price']:,.2f}")
    print(f"  Market Cap  : ${usd['market_cap']:,.0f}")
    print(f"  24h Change  : {usd['percent_change_24h']:+.2f}%")
    print("=" * 40)

    save_to_file(data, "crypto.json")

# Exercise 2: Compare Multiple Cryptos

def compare_cryptos():
    print("\nEnter crypto names separated by comma")
    print(f"Available: {', '.join(CRYPTO_IDS.keys())}")

    coins = input("Cryptos: ").split(",")

    print("\n" + "=" * 60)
    print(f"{'Coin':<15}{'Price($)':<15}{'24h Change'}")
    print("-" * 60)

    results = []

    for coin in coins:
        data = get_crypto(coin.strip())
        if not data:
            continue

        usd = data["quotes"]["USD"]
        print(f"{data['name']:<15}{usd['price']:<15.2f}{usd['percent_change_24h']:+.2f}%")
        results.append(data)

    save_to_file(results, "crypto_comparison.json")

# Exercise 3: POST Request Example

def create_post():
    print("\n=== Create Fake Post ===")
    title = input("Title: ")
    body = input("Body: ")

    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": title, "body": body}

    response = requests.post(url, json=payload)

    print("\nStatus Code:", response.status_code)
    print("Response:")
    print(response.json())

# Exercise 4: Save to JSON File

def save_to_file(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

# Exercise 5: OpenWeatherMap (API KEY OPTIONAL)

def weather_with_api_key(city):
    api_key = os.environ.get("OPENWEATHER_API_KEY")

    if not api_key:
        print(" OPENWEATHER_API_KEY not set.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(" Failed to fetch weather.")
        return

    data = response.json()
    print(f"\n{city.title()} Temperature: {data['main']['temp']}°C")

# DASHBOARD

def dashboard():
    print("\n" + "=" * 55)
    print("   REAL-WORLD API DASHBOARD")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    while True:
        print("\nOptions:")
        print("1. Check Weather")
        print("2. Check Crypto Price")
        print("3. Compare Cryptos")
        print("4. Create POST Request")
        print("5. Quick Dashboard (Delhi + Bitcoin)")
        print("6. Exit")

        choice = input("\nChoose (1-6): ").strip()

        if choice == "1":
            print(f"Available: {', '.join(CITIES.keys())}")
            city = input("City: ")
            display_weather(city)

        elif choice == "2":
            print(f"Available: {', '.join(CRYPTO_IDS.keys())}")
            coin = input("Crypto: ")
            display_crypto(coin)

        elif choice == "3":
            compare_cryptos()

        elif choice == "4":
            create_post()

        elif choice == "5":
            display_weather("delhi")
            display_crypto("bitcoin")

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print(" Invalid choice")


if __name__ == "__main__":
    dashboard()
