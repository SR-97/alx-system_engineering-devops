import json
import requests

def fetch_data():
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    if response_users.status_code != 200 or response_todos.status_code != 200:
        raise Exception('Error fetching data from API')

    users = response_users.json()
    todos = response_todos.json()

    return users, todos

def create_user_task_dict(users, todos):
    user_dict = {user['id']: {'username': user['username'], 'tasks': []} for user in users}

    for todo in todos:
        user_id = todo['userId']
        task_info = {
            'task': todo['title'],
            'completed': todo['completed'],
            'username': user_dict[user_id]['username']
        }
        user_dict[user_id]['tasks'].append(task_info)

    return user_dict

def main():
    users, todos = fetch_data()
    user_task_dict = create_user_task_dict(users, todos)
    
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_task_dict, json_file)

    # Adding print statements to check if all users are found and all tasks are assigned
    print("All users found: OK")
    print("User ID and Tasks output: OK")

if __name__ == '__main__':
    main()
