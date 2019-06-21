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
parser.add_argument('-ow','--overwrite', help='If there files are overwritten if not only new files created.', required=False)

args = vars(parser.parse_args())

#loading variables from comman line



overwrite = False





#
def IMAGPNGgenerateImageResolutions(imageName, resolutions, extraDirectory):


	#need to add .jpeg support
	try:
		image = Image.open(imageName + ".png")
	except:
		image = Image.open(imageName)
		imageName = imageName.replace(".png","")
	size = image.size

	#print "Generating Resolutions"
	#print "    Input File: " + imageName
	#print "    Resolution: " + str(size[0]) + "," + str(size[1])
	width = size[0]
	height = size[1]

	basePath = os.path.dirname(imageName)
	saveName = imageName.replace(basePath + "\\",  basePath + "\\" + extraDirectory)

	for r in resolutions:
		
		newImageName = saveName + "_" + r + ".png"
		
		if overwrite or not os.path.isfile(newImageName):
			print "    Generating for File: " + imageName + "  size: "  + r
			ratio = float(width) / float(height)
			#print "        Generating Resolution: " + r + " ratio: " + str(ratio)
			imageNew = image.resize((int(r), int(int(r)/ratio)), Image.ANTIALIAS)
			quality_val = 95
			imageNew.save(newImageName, 'PNG', quality=quality_val)
		

def IMAGPNGgenerateAllImages(directoryName, resolutions, extraDirectory):
	print "Generating Resolutions for: " + directoryName

	for root, _, files in os.walk(directoryName):
		for f in files:
			fullName = os.path.join(root, f)
			try:
				type= f.split(".")[1]
			except:
				pass
				#print "no file type"

			#time.sleep(1)


			#temp exclusions
			
	
			fileTest = f
			fileTest = fileTest.replace("_1608", "")	#metric 0603
			fileTest = fileTest.replace("_0603", "")	#metric 0603
			fileTest = fileTest.replace("_0402", "")	#metric 0603
			fileTest = fileTest.replace("_1005", "")	#metric 0402

			#make +01 etc okay (fails if more than 10 images
			fileTest = fileTest.replace("_0", "") #So _Top (Top  Images still get generated
			fileTest = fileTest.replace("_T", "") #So _Top (Top  Images still get generated
			fileTest = fileTest.replace("_R", "")    #So _RE (Referene Images still get generated
			fileTest = fileTest.replace("_B", "")	#So _Bottom (Bottom Images still get generated
	
			#make alphabet underscores okay
			fileTest = fileTest.replace("_A", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_B", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_C", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_D", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_E", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_F", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_G", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_H", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_I", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_J", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_K", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_L", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_M", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_N", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_O", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_P", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_Q", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_R", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_S", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_T", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_U", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_V", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_W", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_X", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_Y", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_Z", "")	#So _Bottom (Bottom Images still get generated
			
			
			fileTest = fileTest.replace("_a", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_b", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_c", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_d", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_e", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_f", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_g", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_h", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_i", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_j", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_k", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_l", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_m", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_n", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_o", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_p", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_q", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_r", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_s", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_t", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_u", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_v", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_w", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_x", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_y", "")	#So _Bottom (Bottom Images still get generated
			fileTest = fileTest.replace("_z", "")	#So _Bottom (Bottom Images still get generated
			
			if ".png" in fileTest and not "_" in fileTest:
				imageName = fullName
				IMAGPNGgenerateImageResolutions(imageName, resolutions, extraDirectory)





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
overwrite = False
if args['overwrite'] <> None:
	overwrite = True



if imageName <> "":
	print "Generating for image: "
	IMAGPNGgenerateImageResolutions(imageName, resolutions, extraDirectory)
if directoryName <> "":
	print "Generating for directory: " + directoryName
	IMAGPNGgenerateAllImages(directoryName, resolutions, extraDirectory)



