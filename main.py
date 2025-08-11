import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv('USERNAME')
token = os.getenv('TOKEN')
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph1"

#Step 1: We will register ourself and then run the response.post which is used to give the our data to website and the token can be of our choice
para = {
    "token":os.getenv('TOKEN'),
    "username":os.getenv('USERNAME'),
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint,json=para)
# print(response.text)

#Step 2: after registering we will make a graph which will keep track here comes the authentication part which header
#Headers-usually if we do not use headers out token,graph name,user name and many more things are visible in url and anybody can read it
#headers is used for protection which just show our username and keep aur token safe if someone is sniffing
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN":token
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

#Step 3: We will update our graph by providing todays and quantity of work we did and it will be shown in the graph
update_pixel = f"{graph_endpoint}/{graph_id}"

date = datetime.now()
format_date = date.strftime("%Y%m%d")

pixel_para = {
    "date":format_date,
    "quantity":"5"
}
response = requests.post(url=update_pixel,json=pixel_para,headers=headers)
print(response.text)

#Step 4: If we have provided wrong data then using put method we can change the value of quantity of a particular date
put_pixel = f"{update_pixel}/{format_date}"

put_para = {
    "quantity":"2"
}

response = requests.put(url=put_pixel,json=put_para,headers=headers)
print(response.text)

#Step 5: If we want to delete the data of a particular date then we can use delete func
# response = requests.delete(url=put_pixel,headers=headers)
# print(response.text)