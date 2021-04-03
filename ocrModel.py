import torch

print(torch.cuda.is_available())
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams

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


output = reader.readtext('q.jpg')


img = cv2.imread('q.jpg')
for detection in output:
  top_left = tuple([int(val) for val in detection[0][0]])
  bottom_right = tuple([int(val) for val in detection[0][2]])
  
  img = cv2.rectangle(img,top_left,bottom_right,(255,255,255),-1)

plt.figure(figsize=(10,10))
cv2.imshow("img",img)
cv2.waitKey(0)