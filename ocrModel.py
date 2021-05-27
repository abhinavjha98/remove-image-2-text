import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
import re
import shutil, os
import time
rcParams['figure.figsize'] = 8, 16
img_names = []
reader = easyocr.Reader(['en'])
t1 = time.perf_counter()
import json
f = open("env.json")
data = json.load(f)

for i in data["data"]:
    dir_file = i["dir"]
    file_to_scan = i["file_to_scan"]
f.close

for file_name in os.listdir(dir_file):

    if file_name.split(".")[-1].lower() in file_to_scan:
        output = reader.readtext(file_name)
        count = 0
        for detection in output:
          text = detection[1]
          count += len(re.findall(r'\w+', text))
          if count > (400+10):
            break
        if count < 400:
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
            print("Successfully changed the image")
          except:
            pass
          
        else:
          try:
            shutil.move(file_name,'documents/')
            print("Successfully changed the document")
          except:
            pass
          

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')