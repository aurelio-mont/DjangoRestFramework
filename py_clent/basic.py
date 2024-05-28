import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

response = requests.get(endpoint, params={"a": 111}, json={"query": "hello"})

#print(response.status_code)
#print(response.headers)
#print(response.text)
print(response.json())
