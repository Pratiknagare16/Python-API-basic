import requests

def search_todos():
    print("\n--- Todo Search ---")
    print("Type 'true' to see completed tasks")
    print("Type 'false' to see incomplete tasks")

    status = input("Enter status (true / false): ").lower().strip()

    if status not in ["true", "false"]:
        print(" Please enter only 'true' or 'false'")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"completed": status})
    todos = response.json()

    print(f"\nFound {len(todos)} tasks with completed = {status}\n")

    for i, todo in enumerate(todos[:15], 1):  
        print(f"{i}. {todo['title']}")
        


search_todos()
