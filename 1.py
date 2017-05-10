# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
# cv2.imshow("image", image)
# cv2.waitKey(0)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray)
# cv2.waitKey(0)
hist=cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("Gray Scale HIST")
plt.xlabel("Bins")
plt.ylabel("# of Pixel")
plt.plot(hist)
plt.xlim([0,256])
# plt.show()

chans=cv2.split(image)
colors=('b','g','r')
plt.figure()
plt.title("Flattened")
plt.xlabel("Bins")
plt.ylabel("# of Pixel")
features=[]

# zip is used to zip two quatities togeter as a one list of tuple in the case
for (chan,color) in zip(chans,colors):
	hist=cv2.calcHist([chan],[0],None,[256],[0,256])
	features.extend(hist)

	plt.plot(hist,color=color)
	# plt.show()
	plt.xlim([0,256])

print "flattened feature vector size:%d" %(np.array(features).flatten().shape)

fig=plt.figure()

# histogram for green and blue
ax=fig.add_subplot(131)
hist=cv2.calcHist([chans[1],chans[0]],[0,1],None,[32,32],[0,256,0,256])
p=ax.imshow(hist,interpolation='nearest')
ax.set_title("2D")
plt.colorbar(p)
# plt.show()

hist_total=cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
print "3d Hstogram shape %s with values: %d " %(hist_total.shape,hist_total.flatten().shape[0])