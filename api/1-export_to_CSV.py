import requests
import csv
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

def export_to_csv(employee_id, username, todos_data):
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            csv_writer.writerow([employee_id, username, todo['completed'], todo['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    employee_data, todos_data = fetch_employee_data(employee_id)
    username = employee_data.get('username', 'Unknown User')
    export_to_csv(employee_id, username, todos_data)
