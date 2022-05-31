
from PIL import Image
import numpy as np
import argparse

def threshold(grayimage):
#thresholds a given 2d image
  grayimage[grayimage>127]=255
  grayimage[grayimage<127]=0
  return grayimage

def classifier(imagePath):
'''classifies a given 3d image into day or night image.
Arguments:
   imagePath(str): path of image
returns:
   (str): 'day' or 'night' 
'''
  night,day=0,0
  image2=Image.open(imagePath)
  image=np.array(image2)
  b,g,r=image[:,:,0],image[:,:,1],image[:,:,2]
  gray_b=threshold(b)
  gray_g=threshold(g)
  gray_r=threshold(r)
  gray_b_featurevector=list((gray_b.reshape(1,gray_b.shape[0]*gray_b.shape[1]))[0])
  gray_g_featurevector=list((gray_g.reshape(1,gray_g.shape[0]*gray_g.shape[1]))[0])
  gray_r_featurevector=list((gray_r.reshape(1,gray_r.shape[0]*gray_r.shape[1]))[0])
  final_list=list(zip(gray_b_featurevector,gray_g_featurevector,gray_r_featurevector))
  for i in final_list:
    if i==(0,0,0):
      night+=1
    elif i==(255,255,255):
      day+=1
    else:
      pass
  if(day>night):
    #print('day')
    return 'day'
  else:
    #print('night') 
    return 'night'

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagepath", required=True,
	help="path to input image")
args = vars(ap.parse_args())


try:
	classifier(args['imagepath'])
except Exception as e:
	print(e)














