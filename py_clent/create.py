import requests

endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/products/"

headers = {
    "Authorization": "Bearer e850212f321da20837aede586170e681276d6a57"
}

data = {
    "title": "This is my new product",
    "price": 32.33
}

response = requests.post(endpoint, json=data, headers=headers)


print(response.json())
