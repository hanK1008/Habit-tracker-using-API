import requests
from datetime import datetime

# making habit tracker login values
user_endpoint = "https://pixe.la/v1/users"

# User info
token = "asd484dfsd81sd8946645"
username = "hank"
graph_id= "graph1"

# json file for required user information for api post
user_params = {
    "token": "asd484dfsd81sd8946645",
    "username": "hank",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Comment out the below code after creating the username once
# response = requests.post(url=user_endpoint, json=user_params)
# print(response.text)

# Creating Graph
# actual endpoint https://pixe.la/v1/users/user_id/graphs"
graph_endpoint = f"{user_endpoint}/{username}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

# How to use headers while requesting for API
# Create headers dictionary
headers = {
    "X-USER-TOKEN": token
}


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Adding data to graph
add_graph_data_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime(year= 2023, month=1, day=23)
format_date = today.strftime("%Y%m%d")

graph_data_params = {
    "date": f"{today.strftime('%Y%m%d')}",
    "quantity": "5.0",
}

# connection = requests.post(url= add_graph_data_endpoint, json= graph_data_params, headers= headers)
# print(connection.text)

# updating previous data in the graph using put request
update_graph_data_endpoint = f"{add_graph_data_endpoint}/{format_date}"

update_graph_data_params = {
    "quantity": "10.5"
}

# response = requests.put(url=update_graph_data_endpoint, json=update_graph_data_params, headers=headers)
# print(response.text)

# Deleting data from the graph using put request

response = requests.delete(url=update_graph_data_endpoint, headers=headers)
print(response.text)


