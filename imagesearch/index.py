# important imports
import rgbhistogram 
import argparse
import cPickle
import glob
import cv2
import pprint

# argumet parser
ap=argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,help="Path to dataset of images")
ap.add_argument("-i","--index",required=True,help="Path to index of images")
args=vars(ap.parse_args())

index={}
desc=rgbhistogram.RGBHistogram([8,8,8])

for imagePath in glob.glob(args["dataset"]+"/*.png"):
	# split the last portion of the image
	k=imagePath[imagePath.rfind("/")+1:]
	image=cv2.imread(imagePath)
	features=desc.createHist(image)
	index[k]=features

f=open(args["index"],'w')
f.write(cPickle.dumps(index))
f.close()
# pprint.pprint(index)



