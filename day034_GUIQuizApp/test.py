import requests
import html

# from pprint import pprint

parameters = {"amount": 10, "type": "boolean"}
resoponse = requests.get(url="https://opentdb.com/api.php", params=parameters)
resoponse.raise_for_status()
data = resoponse.json()
print(html.unescape(data["results"][0]["question"]))
