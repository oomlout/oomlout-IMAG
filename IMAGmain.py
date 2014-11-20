#!/usr/bin/python

import sys, os
import time
import Image  #USES PIL library http://www.pythonware.com/products/pil/index.htm

import argparse

parser = argparse.ArgumentParser(description='OOMLOUT-IMAG -- Image Resolution Tool')
parser.add_argument('-im','--image', help='absolute name for a single image to generate resolutions for (no suffix)', required=False)
parser.add_argument('-di','--directory', help='directory to recursivly go through to generate resolutions (ignores all jpg s with "_" in their name', required=False)
parser.add_argument('-re','--resolutions', help='resolutions to generate, seperated by a comma output filename is original image name with _RESOLUTION added', required=False)
parser.add_argument('-ed','--extraDirectory', help='Extra directory to add to generated files for proofing etc. (ie gen/)', required=False)

args = vars(parser.parse_args())

#loading variables from comman line









#
def IMAGgenerateImageResolutions(imageName, resolutions, extraDirectory):


	#need to add .jpeg support
	image = Image.open(imageName + ".jpg")
	size = image.size

	print "Generating Resolutions"
	print "    Input File: " + imageName
	print "    Resolution: " + str(size[0]) + "," + str(size[1])
	width = size[0]
	height = size[1]
	
	basePath = os.path.dirname(imageName)
	saveName = imageName.replace(basePath + "\\",  basePath + "\\" + extraDirectory)
	
	for r in resolutions:
		ratio = float(width) / float(height)
		print "        Generating Resolution: " + r + " ratio: " + str(ratio)
		imageNew = image.resize((int(r), int(int(r)/ratio)), Image.ANTIALIAS)
		quality_val = 95
		imageNew.save(saveName + "_" + r + ".jpg", 'JPEG', quality=quality_val)

def IMAGgenerateAllImages(directoryName, resolutions, extraDirectory):
	"Generating Resolutions for: " + directoryName
	for root, _, files in os.walk(directoryName):
		for f in files:
			fullName = os.path.join(root, f)
			try:
				type= f.split(".")[1]
			except:
				print "no file type"

			#time.sleep(1)

			#make +01 etc okay (fails if more than 10 images
			fileTest = f.replace("_0", "")
			fileTest = fileTest.replace("_T", "") #So _Top (Top  Images still get generated
			fileTest = f.replace("_R", "")    #So _RE (Referene Images still get generated
			fileTest = f.replace("_B", "")	#So _Bottom (Bottom Images still get generated

			if type.lower() in ".jpg" and not "_" in fileTest:
				print "    Generating for File: " + f + "  type: "  + type
				imageName = fullName.split(".")[0]
				IMAGgenerateImageResolutions(imageName, resolutions, extraDirectory)





imageName = ""
if args['image'] <> None:
	imageName = args['image']
	print "Generating Resolutions for Image: " + imageName

directoryName = ""
if args['directory'] <> None:
	directoryName = args['directory']
	print "Genrating Resolutions for Directory: " + directoryName

resolutionsString = ""
resolutions = [300]
if args['resolutions'] <> None:
	resolutionsString = args['resolutions']
	resolutions = resolutionsString.split(",")

print "Resolutions: "
for b in resolutions:
	print "    " + b

extraDirectory=""
if args['extraDirectory'] <> None:
	extraDirectory = args['extraDirectory']



if imageName <> "":
	IMAGgenerateImageResolutions(imageName, resolutions, extraDirectory)
if directoryName <> "":
	IMAGgenerateAllImages(directoryName, resolutions, extraDirectory)



