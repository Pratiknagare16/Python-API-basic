import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

users = response.json()

print("Exercise 2 - All Users\n")

for user in users:
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("-" * 30)
