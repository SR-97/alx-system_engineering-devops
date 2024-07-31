#!/usr/bin/python3
"""
This script retrieves data from a REST API and exports the TODO list progress
of all employees to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(base_url + "users").json()
    todos = requests.get(base_url + "todos").json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_todos = [todo for todo in todos if todo.get("userId") == user_id]
        
        tasks_list = []
        for todo in user_todos:
            tasks_list.append({
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })
        
        all_tasks[user_id] = tasks_list

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(all_tasks, file)
