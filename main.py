import requests
from datetime import datetime
import os

# CONSTANTS
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("PIXELA_USER")
PIX_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": PIX_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": PIX_TOKEN,
}

graph1_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

graph_update_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": int(input("How many hours did you code today?")),
}

# response = requests.post(url=graph1_endpoint, json=graph_update_config, headers=headers)
# print(response.text)

# update_pixel_endpoint = f"{graph1_endpoint}/{today.strftime('%Y%m%d')}"
#
# update_pixel_config = {
#     "quantity": "0"
# }

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_pixel_endpoint, headers=headers)
# print(response.text)
