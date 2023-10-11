'''Using what you did in the task #0, extend your Python script to export data in the JSON format.'''
import json
import requests
import sys

def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"
    
    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)
    
    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)
    
    employee_data = employee_response.json()
    todos_data = todos_response.json()
    return employee_data, todos_data

def export_to_json(employee_id, username, todos_data):
    json_data = {str(employee_id): []}
    for todo in todos_data:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        }
        json_data[str(employee_id)].append(task_info)
    
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    employee_data, todos_data = fetch_employee_data(employee_id)
    username = employee_data.get('username', 'Unknown User')
    export_to_json(employee_id, username, todos_data)
