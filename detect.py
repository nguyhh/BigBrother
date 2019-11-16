import io
import os
from PIL import Image
import requests

# get all info
r1 = requests.get('https://pidgey2.azurewebsites.net/yulcode/employees')

# Step 1: for loop to retrieve id and name
r1obj = r1.json()
path = os.getcwd()
for i in r1obj:
    os.mkdir(str(i["id"]))
    

# Step 2: for loop to retrieve picture
for i in r1obj:
    id = i["id"]
    print(id)
    r2 = requests.get('https://pidgey2.azurewebsites.net/yulcode/employees/' + str(id) + '/photo', stream = True)
    with io.BytesIO(r2.content) as f:
        with Image.open(f) as img:
            img.save(path + "/" + str(id) + "/" + str(i["name"]) + ".jpeg")


