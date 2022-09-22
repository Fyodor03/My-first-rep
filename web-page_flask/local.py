import requests

res = requests.put("http://127.0.0.1:8000/api/courses/2", {"name": "Golang", "videos": 5})
# res = requests.post("http://127.0.0.1:8000/api/courses/4", {"name": "PHP", "videos": 15})
print(res.json())
