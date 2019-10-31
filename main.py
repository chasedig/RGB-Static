#@Author = "Chase Carlson"
#@Name = "Average Color"
#@Date = 10/30/2019
#@Version = 1.0

import numpy as np
import matplotlib.pyplot as plt
import random
import secrets
import cv2

img_array = np.zeros((100,100,3), np.uint8)
for i in range(100):
	for j in range(100):
			img_array[i,j] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


		


imgplot = plt.imshow(img_array)
print(img_array)
plt.show(imgplot)
cv2.imwrite("rgbstatic.png",img_array)

