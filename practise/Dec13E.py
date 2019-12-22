import requests
import json

parm={"username":"corey","password":"testing"}
r = requests.get("https://httpbin.org/basic-auth/abcd/124", auth=('abcd','124'))
print(r.status_code)
print(r.text)