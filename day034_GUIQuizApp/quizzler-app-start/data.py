import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
resoponse = requests.get(url="https://opentdb.com/api.php", params=parameters)
resoponse.raise_for_status()
data = resoponse.json()
question_data = data["results"]
