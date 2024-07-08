import requests

response = requests.get("https://catfact.ninja/breeds")
print(response.status_code)
print(response.json())
