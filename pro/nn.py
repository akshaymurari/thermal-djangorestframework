import requests
import json
r=requests.get(url="http://127.0.0.1:8000/get/1")
print(r.json())