import json
import requests

def fetch_data():
    # Fetch users data
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()

    # Fetch todos data
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos_response.json()

    # Prepare data in the required format
    all_data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        all_data[user_id] = []
        
        user_tasks = [task for task in todos if task['userId'] == user_id]
        for task in user_tasks:
            task_info = {
                'username': username,
                'task': task['title'],
                'completed': task['completed']
            }
            all_data[user_id].append(task_info)

    # Write data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_data, json_file)

if __name__ == '__main__':
    fetch_data()

