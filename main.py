import requests

#connects with link
response = requests.get("https://randomfox.ca/floof")

#reads Json file and prints random image in print function
fox = response.json()
print(fox['image'])