#RGB-Static
#main.py
#10/26/2019
#Chase Carlson

import numpy as np
import matplotlib.pyplot as plt
import random
import secrets
import cv2

img_array = np.zeros((100,100,3), np.uint8)
for i in range(100):
	for j in range(100):
			img_array[i,j] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
			img_array[i,j] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


		


imgplot = plt.imshow(img_array)
print(img_array)
plt.show(imgplot)
cv2.imwrite("rgbstatic.png",img_array)

