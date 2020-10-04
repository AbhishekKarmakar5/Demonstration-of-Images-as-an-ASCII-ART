
import cv2
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

image = cv2.imread('Image.png')
#image = cv2.imread('Capture.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imwrite("BLKimage.png",th3)

img_data = PIL.Image.open('BLKimage.png')
img_arr = np.array(img_data) 
print(img_arr.shape)

img_convert = img_data.resize((105,150))
img_arr_convert = np.array(img_convert) 
print(img_arr_convert.shape)

for i in range(img_arr_convert.shape[0]):
	for j in range(img_arr_convert.shape[1]):

		if(j!=(img_arr_convert.shape[1]-1)):
			if(img_arr_convert[i][j]==0):
				print("*",end=" ")
			else:
				print(" ",end=" ")
		else:
			if(img_arr_convert[i][j]==0):
				print("*")
			else:
				print(" ")			


plt.imshow(img_convert, cmap="gray") 
plt.show() 


