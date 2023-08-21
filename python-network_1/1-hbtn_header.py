"""Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python 1-hbtn_header.py <URL>")
        return

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in the response header.")
    else:
        print(f"Request to {url} failed with status code: {response.status_code}")

if __name__ == "__main__":
    main()
