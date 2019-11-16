# import the necessary packages
# from imutils import paths
import numpy as np
# import argparse
# import imutils
# import pickle
import cv2
import os
import requests
# import scikit-learn ## matching people
import io
from PIL import Image

# get all info
r1 = requests.get('https://pidgey2.azurewebsites.net/yulcode/employees')

# Step 1: for loop to retrieve id and name
r1obj = r1.json()
path = os.getcwd()
for i in r1obj:
    os.mkdir(path + "/dataset/" + str(i["name"]))


# Step 2: for loop to retrieve picture
for i in r1obj:
    id = i["id"]
    name = i["name"]
    print(id)
    r2 = requests.get('https://pidgey2.azurewebsites.net/yulcode/employees/' + str(id) + '/photo', stream = True)
    with io.BytesIO(r2.content) as f:
        with Image.open(f) as img:
            img.save(path + "/dataset/" + str(name) + "/" + str(i["name"]) + ".jpeg")
