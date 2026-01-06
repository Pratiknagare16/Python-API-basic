import requests
import time
import logging
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException


logging.basicConfig(level=logging.INFO)



def safe_api_request(url, retries=3, timeout=5):
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Requesting URL: {url} (Attempt {attempt})")

            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return {"success": True, "data": response.json()}

        except (ConnectionError, Timeout) as e:
            logging.error(f"Network error: {e}")

        except HTTPError as e:
            logging.error(f"HTTP error: {e}")
            return {"success": False, "error": f"HTTP Error {e.response.status_code}"}

        except RequestException as e:
            logging.error(f"Request error: {e}")

        if attempt < retries:
            print("Retrying in 2 seconds...\n")
            time.sleep(2)

    return {"success": False, "error": "Failed after 3 attempts"}



def validate_crypto_response(data):
    if "quotes" not in data:
        return False, "Missing 'quotes' in response"

    if "USD" not in data["quotes"]:
        return False, "Missing USD price data"

    return True, "Valid response"



def fetch_crypto():
    print("\n=== Crypto Price Checker ===")
    coin = input("Enter coin (btc-bitcoin, eth-ethereum): ").strip().lower()

    if not coin:
        print("Coin name cannot be empty.")
        return

    url = f"https://api.coinpaprika.com/v1/tickers/{coin}"
    result = safe_api_request(url)

    if not result["success"]:
        print("Error:", result["error"])
        return

    data = result["data"]
    valid, message = validate_crypto_response(data)

    if not valid:
        print("Invalid API response:", message)
        return

    usd = data["quotes"]["USD"]

    print(f"\n{data['name']} ({data['symbol']})")
    print(f"Price: ${usd['price']:,.2f}")
    print(f"24h Change: {usd['percent_change_24h']:+.2f}%")



def demo_error_handling():
    print("\n=== Error Handling Demo ===")

    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/99999",
        "https://invalid-domain-123456.com",
    ]

    for url in urls:
        print(f"\nTesting: {url}")
        result = safe_api_request(url)

        if result["success"]:
            print("Success:", str(result["data"])[:50])
        else:
            print("Failed:", result["error"])



def main():
    while True:
        print("\n==========================")
        print("  Robust API Demo App")
        print("==========================")
        print("1. Test error handling")
        print("2. Check crypto price")
        print("3. Exit")

        choice = input("Choose (1-3): ")

        if choice == "1":
            demo_error_handling()
        elif choice == "2":
            fetch_crypto()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
