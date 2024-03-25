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

	# checks whether frames were extracted 
	success = 1

	try:
		while success: 

			# vidObj object calls read 
			# function extract frames 
			success, image = vidObj.read() 
			
			# Saves the frames with frame-count 
			savedFileName = path + "\\images\\" + "frame" + str(count) + ".jpg"
			print(savedFileName)
			
			cv2.imwrite(str(savedFileName), image) 
	
			count += 1
	except: 
		print("End of images")
	print(count)
	return count


# Driver Code 
if __name__ == '__main__': 
	from crop import crop #the python file 
	import time
	from imageToText import *
	# Calling the function 
	#FrameCapture("Z:\\0_NewOBSOutput\\demo.mp4") #"C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
	directory = "C:\\Users\\nicpi\\OneDrive\\Documents\\Python_VideoToText_DroidScriptVideo_GPS\\GetGPSFromDroidScript"
	videoName = "demo.mp4"
	counter = FrameCapture(directory,videoName)
	for i in range(counter): 
		imageName = "frame" + str(i) + ".jpg"
		crop(directory+ "\\images\\", imageName)
		imageToText(directory + "\\images\\", imageName)
		time.sleep(0.1) #print(i)