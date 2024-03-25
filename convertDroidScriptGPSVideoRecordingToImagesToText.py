#https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/
# Program To Read video 
# and Extract Frames 
import cv2 
import re 

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
			
			if skip == skipLimit: #every (~55/skip) FPS, a frame is saved (idk how to word it, but its less frames :) )
				cv2.imwrite(str(savedFileName), image) 
				skip = 0
				count += 1
				print(savedFileName)
			skip +=1
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

	buffer = ""
	infoBuffer=[0]*6 #place holders, will be a buffer for when I save to a CSV file 
	auth = ["L", "S", "B", "A"] #first letter of important info to rip
	auth2 = ["a","n", "p", "e", "l", "c"] #second letter of important info to rip 
  
	for i in range(counter): 
		print("----------- " + str(i) + " -----------")
		imageName = "frame" + str(i) + ".jpg"
		crop(directory+ "\\images", imageName) #Crops the image file 
		text = imageToText(directory + "\\images", imageName) #Extracts text from the image file
		os.remove(directory + "\\images\\" + imageName) #deletes the image file once it has read the text
		print("------------------------------")
		print(text)
		time.sleep(1) #print(i)
  
		#attempting to make the CSV buffer shit here (MOVE TO SEPORATE FILE LATER )
		text = text.split('|')
		holder = []
		#text = text.split('\\n')
		tempCounter = 0
		for i in text: 
			temp = text[tempCounter].split(',')
			print(temp)
			for j in temp:
				holder.append(j)
			#print()
			tempCounter +=1
		print(holder)

		tempCounter = 0 
		for i in holder: #make it ONLY numbers now 
			print(i)
			output = re.findall(r"[-+]?\d*\.\d+|\d+", i)
			holder[tempCounter] = float(output[0])
			tempCounter += 1
		print(holder)
		#print(temp)
		tempCounter = 0
		#for i in text:
		#	if (i or buffer) in auth :
		#		if i in auth: #on the next pass, this will help 
		#			buffer = i
		#		else: #means that BUFFER is the one that is in auth, meanings its time to check the 2nd char 
#
#					if i == auth2[0]: #a -> La -> Latitude
#						infoBuffer[0] = text[tempCounter + 3:{NUMBER HERE FOR THE LOCATION OF THE FIRST BAR}]
#			tempCounter += 1

       #get lat
       #get lon
       #get spd
       #get bear
       #get alt
	   #get accu
  
  
  
  
  
