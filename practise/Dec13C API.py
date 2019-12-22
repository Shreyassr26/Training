import requests
import json
#get scenarios
parm={"page":2,"count":4}
r = requests.get("https://httpbin.org/get",params=parm)
print(r.status_code)
print(r.text, type(r.text))
json_data = json.loads(r.text)
print(json_data)
# print(type(json_data))
# print(r.json(), type(r.json()))
