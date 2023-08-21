"""Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

def main():
    url = sys.argv[1]
    response = requests.get(url)
    
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("[Got]\nX-Request-Id not found in response header.\n(43 chars long)")

if __name__ == "__main__":
    main()
