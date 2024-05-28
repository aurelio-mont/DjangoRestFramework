import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/products/2/update/"

data = {
    "title": "This is my UPDATED product",
    "price": 199.99
}

response = requests.put(endpoint, json=data)

#print(response.status_code)
#print(response.headers)
#print(response.text)
print(response.json())
