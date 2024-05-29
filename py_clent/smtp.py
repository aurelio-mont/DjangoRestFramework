import requests

endpoint = "http://127.0.0.1:8000/api/email/"

headers = {
    "Authorization": "Bearer e850212f321da20837aede586170e681276d6a57"
}

data = {
    "subject": "This is my new product",
    "to_email": "aurelio.mont@me.com",
    "message": "This is a test email"
}

#response = requests.post(endpoint, json=data, headers=headers)
response = requests.post(endpoint, json=data, headers=headers)


print(response.json())
