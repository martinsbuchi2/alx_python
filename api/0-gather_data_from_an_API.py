'''Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.'''
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

def display_todo_progress(employee_name, todos_data):
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print(f"    {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    employee_data, todos_data = fetch_employee_data(employee_id)
    employee_name = employee_data.get('name', 'Unknown Employee')
    display_todo_progress(employee_name, todos_data)
