import requests
import os
from datetime import datetime


PIXELA_KEY = os.environ.get('PIXELA_KEY')
USERNAME = "charis"
GRAPH_ID = "graph1"


headers = {
    "X-USER-TOKEN": PIXELA_KEY
}


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#---------- CREATE ACCOUNT --------------
# response = requests.post(url = pixela_endpoint, json = user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "my_prog_graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

#---------- CREATE GRAPH -----------------------------
# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)


put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# ****************** EXTRA CODE **********************************************************************
# IF YOU WANT TO TYPE A PREVIOUS DATE(with example values that can be input from user if you want to):
# date = datetime(year= 2023, month= 10,day= 1) 

current_date = datetime.now().strftime("%Y%m%d")
activity_duration = input(f"How many hours did you code on {current_date[0:4]}-{current_date[4:6]}-{current_date[6:]}?\n")

pixel_config = {
    "date": current_date,
    "quantity": activity_duration
}

#---------- CREATE PIXEL ---------------------------------
# response = requests.post(url = put_pixel_endpoint, json = pixel_config, headers = headers)


update_pixel_endpoint = f"{put_pixel_endpoint}/{current_date}"

activity_duration = input(f"Update the hours you coded on {current_date[0:4]}-{current_date[4:6]}-{current_date[6:]}?\n")

update_pixel_config = {
    "quantity": activity_duration
}

#---------- UPDATE PIXEL ---------------------------------
# response = requests.put(url = update_pixel_endpoint, json = update_pixel_config, headers = headers)

delete_pixel_endpoint = update_pixel_endpoint

#---------- UPDATE PIXEL ---------------------------------
response = requests.delete(url = delete_pixel_endpoint, headers = headers)
print(response.text)