import torch
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
import re
import shutil, os

rcParams['figure.figsize'] = 8, 16

reader = easyocr.Reader(['en'])


import pickle
# Pkl_Filename = "ocrModel.pkl" 
# with open(Pkl_Filename, 'wb') as file:  
#     pickle.dump(reader, file)
import torch
# torch.save(reader, "Pickle_RL_Model.h5")

# the_model = torch.load("Pickle_RL_Model.h5")
# the_model

import os

for file_name in os.listdir("E:/IntechHub Solution/modelOCR/"):
  
    if file_name.split(".")[-1].lower() in {"jpeg", "jpg", "png"}:
        output = reader.readtext(file_name)
        count = 0
        for detection in output:
          text = detection[1]
          count += len(re.findall(r'\w+', text))
          if count > 70:
            break
        if count < 60:
          img = cv2.imread(file_name)
          for detection in output:
            top_left = tuple([int(val) for val in detection[0][0]])
            bottom_right = tuple([int(val) for val in detection[0][2]])
            
            img = cv2.rectangle(img,top_left,bottom_right,(255,255,255),-1)
            # plt.figure(figsize=(10,10))
            # cv2.imshow("img",img)
            # cv2.waitKey(0)
          new_file = file_name
          file_names = file_name.split(".")
          new_file_name = "updated_"+file_names[0]+"."+file_names[1]
          cv2.imwrite("images/"+new_file_name, img)
          try:
            shutil.move(file_name,'images/')
          except:
            pass
          
        else:
          try:
            shutil.move(file_name,'documents/')
          except:
            pass
          

# output = reader.readtext('q1.jpeg')
# count = 0
# for detection in output:
  
#   text = detection[1]
#   count += len(re.findall(r'\w+', text))
#   print(count)

# if count < 60:
#   img = cv2.imread('q.jpg')
#   for detection in output:
#     top_left = tuple([int(val) for val in detection[0][0]])
#     bottom_right = tuple([int(val) for val in detection[0][2]])
    
#     img = cv2.rectangle(img,top_left,bottom_right,(255,255,255),-1)
#     # plt.figure(figsize=(10,10))
#     # cv2.imshow("img",img)
#     # cv2.waitKey(0)
#     files="q.jpg"
#     shutil.move(files,'images/')
# else:
#   files = "q1.jpeg"
#   shutil.move(files,'documents/')
#   print("pass")
