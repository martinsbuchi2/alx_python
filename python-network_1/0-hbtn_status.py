"""Python script that fetches https://alu-intranet.hbtn.io/status"""

import requests
res = requests.get('https://alu-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(res.text)))
print("\t- type: {}".format(res.text))