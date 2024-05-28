import requests

product_id = input("Enter product id: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid product id")
if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"


response = requests.delete(endpoint)

#print(response.status_code)
#print(response.headers)
#print(response.text)
print(response.status_code, response.status_code == 204)
