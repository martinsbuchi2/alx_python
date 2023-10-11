# '''Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.'''

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee data
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()

    # Fetch TODO list for the employee
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Calculate completed tasks and total tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)

    # Print employee TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
