import requests

url = "https://jsonplaceholder.typicode.com/users/5"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("User Found!")
    print(data)
else:
    print("Resource not found!")
