#https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/
# Program To Read video 
# and Extract Frames 
import cv2 

# Function to extract frames 
def FrameCapture(path): 

	# Path to video file 
	vidObj = cv2.VideoCapture(path) 

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
			cv2.imwrite("frame%d.jpg" % count, image) 

			count += 1
	except: 
		print("End of images")
	#print(count)
	return count


# Driver Code 
if __name__ == '__main__': 
	from crop import crop #the python file 
	# Calling the function 
	#FrameCapture("Z:\\0_NewOBSOutput\\demo.mp4") #"C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
	directory = "C:\\Users\\nicpi\\OneDrive\\Documents\\Python_VideoToText_DroidScriptVideo_GPS\\GetGPSFromDroidScript"
	videoName = "demo.mp4"
	counter = FrameCapture(directory + "\\" + videoName)
	for i in range(counter): 
		crop(directory, "frame" + str(i) + ".jpg")
		#print(i)