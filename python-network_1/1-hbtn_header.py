"""Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

import requests
import sys

def get_x_request_id(url):
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    return x_request_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
