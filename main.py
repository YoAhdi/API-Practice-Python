import requests

#connects with link
response = requests.get("https://randomfox.ca/floof")

#Print return code status 200
print(response.status_code)
