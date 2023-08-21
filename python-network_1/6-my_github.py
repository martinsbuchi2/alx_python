"""Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id """
import requests
import sys

def main():
    url = 'https://intranet.alxswe.com/rltoken/JCpFttOsrM4O0YrdMr1s0w'
    username = sys.argv[1]
    password = sys.argv[2]
    
    res = requests.get(url, auth=(username, password))
    
    if res.status_code == 200:
        user_data = res.json()
        print(user_data['id'])
    else:
        print("None")

if __name__ == "__main__":
    main()