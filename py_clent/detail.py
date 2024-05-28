import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/products/2/"

response = requests.get(endpoint)

#print(response.status_code)
#print(response.headers)
#print(response.text)
print(response.json())
