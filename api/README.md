# API

## Objectives

* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

## Resources

1. [What is an API](https://intranet.alxswe.com/rltoken/CRB8vFQ4CMWEDGoXxe9xIA)
2. [What is an API? In English, please](https://intranet.alxswe.com/rltoken/nmdvTgdZH9JCSNJo19sA0Q)
3. [What is a REST API](https://intranet.alxswe.com/rltoken/2bfOp8WycFmfCeion6vx4A)
4. [What are microservices](https://intranet.alxswe.com/rltoken/rZbEFi14t48LMjdYzWyqEQ)
5. [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://intranet.alxswe.com/rltoken/maJqoGCnAPzDho1WsQSEfw)

## Task 0 - Gather data from an API

Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

NB: The endpoint for access specific TODO items for an employee with ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos and the endpoint to get specific employee details will be https://jsonplaceholder.typicode.com/users/1

Requirements:

* You must use urllib or requests module
* The script must accept an integer as a parameter, which is the employee ID
* The script must display on the standard output the employee TODO list progress in this exact format:
     * First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS): 
     where:
         * EMPLOYEE_NAME: name of the employee
         * NUMBER_OF_DONE_TASKS: number of completed tasks
         * TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
         * Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

## Task 1 - Export to CSV

Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

* Records all tasks that are owned by this employee
* Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
* File name must be: USER_ID.csv

## Task 2 - Export to JSON

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

* Records all tasks that are owned by this employee
* Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
* File name must be: USER_ID.json

## Task 3 - Dictionary of list of dictionaries

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

* Records all tasks from all employees
* Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
* File name must be: todo_all_employees.json
