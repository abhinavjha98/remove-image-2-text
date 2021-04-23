import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
import re
import shutil, os

rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])

import json
f = open("env.json")
data = json.load(f)

for i in data["data"]:
    dir_file = i["dir"]
    count_data = int(i["count"])
    file_to_scan = i["file_to_scan"]
f.close

for file_name in os.listdir(dir_file):

    if file_name.split(".")[-1].lower() in file_to_scan:
        output = reader.readtext(file_name,low_text=0.3,text_threshold=0.4)
        count = 0
        img = cv2.imread(file_name)
        for detection in output:
          top_left = tuple([int(val) for val in detection[0][0]])
          bottom_right = tuple([int(val) for val in detection[0][2]])
          
          img = cv2.rectangle(img,top_left,bottom_right,(255,255,255),-1)
          
        new_file = file_name
        file_names = file_name.split(".")
        new_file_name = "updated_"+file_names[0]+"."+file_names[1]
        cv2.imwrite("images/"+new_file_name, img)
        try:
          shutil.move(file_name,'images/')
        except:
          pass
          
        
          

