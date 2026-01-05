import requests

url = "https://jsonplaceholder.typicode.com/posts/5"
response = requests.get(url)

print("Exercise 1 - Post 5")
print("Status Code:", response.status_code)
print(response.json())
print("-" * 40)




