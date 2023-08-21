"""Python script that fetches https://alu-intranet.hbtn.io/status"""

import requests
def main():    
    res = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
    
if __name__ == "__main__":
    main()