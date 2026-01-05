import requests

url = "https://jsonplaceholder.typicode.com/users/5"
response = requests.get(url)

data = response.json()

print("User 5 Phone Number:", data["phone"])
