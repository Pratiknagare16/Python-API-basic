import requests

url = "https://jsonplaceholder.typicode.com/posts/999"
response = requests.get(url)

print("Exercise 3 - Invalid Post")
print("Status Code:", response.status_code)
print("Response:", response.json())
