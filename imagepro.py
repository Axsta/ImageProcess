import cv2
import numpy as np
from matplotlib import pyplot as plt

#Grey Scaling
image = cv2.imread('pothole.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Gaussian Filter
blur = cv2.GaussianBlur(gray_image,(5,5),0)

#Segmentation : Otsu's method 
ret, thresh = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal (Opening morphology)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# sure background area (Dilation morphology)
sure_bg = cv2.dilate(opening,kernel,iterations = 1)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(image,markers)
image[markers == -1] = [255,0,0]


#Canny Edge Detection
edges = cv2.Canny(image,100,200)

plt.subplot(221),plt.imshow(gray_image,cmap = 'gray')
plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur,cmap = 'gray')
plt.title('Noise Removed Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(image,cmap = 'gray')
plt.title('Segmented Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Detected Image'), plt.xticks([]), plt.yticks([])
plt.savefig('edge.png')
plt.show()
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
