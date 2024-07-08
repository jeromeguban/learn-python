import requests

parameters = {
    "name": 'Edward',
}
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
response = requests.get("https://api.nationalize.io", params=parameters)
print(response.status_code)
print(response.json())
