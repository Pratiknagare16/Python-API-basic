import requests

url = "https://jsonplaceholder.typicode.com/posts/1/comments"
response = requests.get(url)

comments = response.json()

print("Total comments on Post 1:", len(comments))
