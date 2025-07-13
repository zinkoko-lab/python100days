import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")
pixela_endpoint = "https://pixe.la/v1/users"

# Create a user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@jin711 , it is your profile page!","isSuccess":true}

# Create a new pixelation graph definition.

# END POINT = /v1/users/<username>/graphs
graph_end_point = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "My Working Hours",
    "timezone": "Asia/Tokyo",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.put(
#     url=graph_end_point,
#     json=graph_config,
#     headers=headers,
# )
# print(response.text)


# Post a Pixel to the graph
graph1_end_point = f"{graph_end_point}/{graph_id}"
today = datetime.now().today()
TODAY = today.strftime("%Y%m%d")
print(TODAY)
post_pixel_json = {
    "date": TODAY,
    "quantity": "500.0",
}

# response = requests.post(url=graph1_end_point, json=post_pixel_json, headers=headers)
# response.raise_for_status()
# print(response.text)

# Update predefined pixelation graph definitions.
# END POINT = /v1/users/<username>/graphs/<graphID>
end_point = graph1_end_point

graph_config = {
    "timezone": "Asia/Tokyo",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.put(
#     url=graph1_end_point,
#     json=graph_config,
#     headers=headers,
# )
# print(response.text)

# Delete the registered "Pixel".

# $ curl -X DELETE https://pixe.la/v1/users/a-know/graphs/test-graph/20180915 -H 'X-USER-TOKEN:thisissecret'
# {"message":"Success.","isSuccess":true}

date = today - timedelta(days=3)
DATE = date.strftime("%Y%m%d")
print(DATE)
while DATE != TODAY:
    URL = f"{end_point}/{DATE}"
    response = requests.delete(url=URL, headers=headers)
    print(response.text)
    date += timedelta(days=1)
    DATE = date.strftime("%Y%m%d")
