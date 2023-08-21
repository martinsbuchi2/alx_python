"""Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys
def main():
    
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
        
    payload = {'q': q}
    res = requests.post(url, data=payload)
    
    
    try:
        json_data = res.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()