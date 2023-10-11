'''Using what you did in the task #0, extend your Python script to export data in the JSON format.'''

import json
import requests

# Fetch users and tasks data
users_response = requests.get("https://jsonplaceholder.typicode.com/users")
tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")

users_data = users_response.json()
tasks_data = tasks_response.json()

# Create a dictionary to store tasks for all employees
all_tasks_dict = {}

# Populate tasks dictionary
for user in users_data:
    user_id = user["id"]
    username = user["username"]
    user_tasks = []
    
    for task in tasks_data:
        if task["userId"] == user_id:
            task_info = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            user_tasks.append(task_info)
    
    all_tasks_dict[user_id] = user_tasks

# Export data to JSON file
with open("todo_all_employees.json", "w") as json_file:
    json.dump(all_tasks_dict, json_file, indent=4)

print("Data exported to todo_all_employees.json")
