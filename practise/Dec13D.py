import requests
import json
#post scenarios

parm={"username":"corey","password":"testing"}
r = requests.post("https://httpbin.org/get", data=parm)
print(r.status_code)
print(r.text)