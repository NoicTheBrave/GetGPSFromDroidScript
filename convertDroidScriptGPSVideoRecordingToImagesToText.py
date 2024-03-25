#https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/
# Program To Read video 
# and Extract Frames 
import cv2 

# Function to extract frames 
def FrameCapture(path, fileName): 

	# Path to video file 
	vidObj = cv2.VideoCapture(path + "\\" + fileName) 

	# Used as counter variable 
	count = 0
 
	#Screen videos record around 55-60FPS, unless you want ur video of +30 minutes to take you ~16.5 min JUST to convert frames (tested myself), then you are going to wanna skip frames
	skip = 0
	skipLimit=55 #14 #55/14 = (about) 4 images 

	# checks whether frames were extracted 
	success = 1

	try:
		while success: 

			# vidObj object calls read 
			# function extract frames 
			success, image = vidObj.read() 
			
			# Saves the frames with frame-count 
			savedFileName = path + "\\images\\" + "frame" + str(count) + ".jpg"
<<<<<<< HEAD
			
			if skip == skipLimit: #every (~55/skip) FPS, a frame is saved (idk how to word it, but its less frames :) )
				cv2.imwrite(str(savedFileName), image) 
				skip = 0
				count += 1
				print(savedFileName)
			skip +=1
=======
			print(savedFileName)
			
			cv2.imwrite(str(savedFileName), image) 
	
			count += 1
>>>>>>> c08be3db4bc5037b6e621ee48d9ab8b6936eaa74
	except: 
		print("End of images")
	print(count)
	return count


# Driver Code 
if __name__ == '__main__': 
	from crop import crop #the python file 
	import time
	from imageToText import *
	import os
	# Calling the function 
	#FrameCapture("Z:\\0_NewOBSOutput\\demo.mp4") #"C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
	directory = "C:\\Users\\nicpi\\OneDrive\\Documents\\Python_VideoToText_DroidScriptVideo_GPS\\GetGPSFromDroidScript"
	videoName = "demo.mp4"
	counter = FrameCapture(directory,videoName)
	for i in range(counter): 
		print("----------- " + str(i) + " -----------")
		imageName = "frame" + str(i) + ".jpg"
<<<<<<< HEAD
		crop(directory+ "\\images", imageName) #Crops the image file 
		text = imageToText(directory + "\\images", imageName) #Extracts text from the image file
		os.remove(directory + "\\images\\" + imageName) #deletes the image file once it has read the text
		print("------------------------------")

=======
		crop(directory+ "\\images\\", imageName)
		imageToText(directory + "\\images\\", imageName)
>>>>>>> c08be3db4bc5037b6e621ee48d9ab8b6936eaa74
		time.sleep(0.1) #print(i)