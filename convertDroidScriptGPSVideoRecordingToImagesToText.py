#https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/
# Program To Read video 
# and Extract Frames 
import cv2 
import re 
from checkForNumbers import *

DEVELOPMENT = 0 #0 = RUN AS NORMAL ||| 1 = DISABLES GENERATING NEW IMAGES, CROPPING THEM, AND ANY OTHER FEATURES DOWN THE ROAD AS NEED BE (mainly cause I dont need this done avery time to test 1 feature sooooo)

# Function to extract frames 
def FrameCapture(path, fileName): 

	# Path to video file 
	vidObj = cv2.VideoCapture(path + "\\" + fileName) 

	# Used as counter variable 
	count = 0 #this is the Image # counter 
 
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
				if DEVELOPMENT == 0:
					cv2.imwrite(str(savedFileName), image) 
				skip = 0
				count += 1
				#print(savedFileName)
				print(count)
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
	
	#if DEVELOPMENT == 0: #if 0 -> Development is COMPLETE
	#	FrameCapture("Z:\\0_NewOBSOutput\\demo.mp4") #"C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
	
	directory = "C:\\Users\\nicpi\\OneDrive\\Documents\\Python_VideoToText_DroidScriptVideo_GPS\\GetGPSFromDroidScript"
	videoName = "demo.mp4"
 
	#----------RE-ENABLE AFTER DEVELOPMENT IS COMPLETE------------
	if DEVELOPMENT == 0:
		counter = FrameCapture(directory,videoName)
	else:
		counter = len(os.listdir(directory + "\\images\\"))
		print("COUNTER: " + str(counter))



	buffer = ""
	infoBuffer=[0]*6 #place holders, will be a buffer for when I save to a CSV file 
	auth = ["L", "S", "B", "A"] #first letter of important info to rip
	auth2 = ["a","n", "p", "e", "l", "c"] #second letter of important info to rip 

	Lat = [] #latitude
	Long = [] #Longitude 
	Spd = [] #Speed (idk what units this is in, but it seams to work when you are in a car...)
	Bear = [] #bearing
	Alt = [] #Altitude
	Accu = [] #Accuracy...? I believe (not sure what this is w/ refference to but okay)


	for i in range(counter): 
		print("----------- " + str(i) + " -----------")
		imageName = "frame" + str(i) + ".jpg"
		crop(directory+ "\\images", imageName) #Crops the image file 

		text = imageToText(directory + "\\images", imageName) #Extracts text from the image file
		
		#--------RE-ENABLE AFTER DEVELOPMENT IS COMPLETE: DELETE'S IMAGES AFTER DONE WITH PROCESS-----
		#if DEVELOPMENT == 0:
		#	os.remove(directory + "\\images\\" + imageName) #deletes the image file once it has read the text

		print("------------------------------")
		print(text)
		#time.sleep(1) #print(i)
  
		#attempting to make the CSV buffer shit here (MOVE TO SEPORATE FILE LATER )
		text = text.split('|')
		holder = []
		#text = text.split('\\n')
		tempCounter = 0
		for i in text: 
			temp = text[tempCounter].split(',') #Apparently sometimes PERIODS can be mistaken as commas... sooo
	
			#print("TEMP: " + str(temp))
			for j in temp:
				holder.append(j)
			#print()
			tempCounter +=1
		print("HOLDER" + str(holder))
  
		#SOMETIMES the pgm mistakes "." -> "," Following Code-section corrects that
		if len(holder) > 6: #should always be 6, unless it mistakens a period as a comma! then there's at min. 7 items in there 0_0
			#If this happens, this means that ONE of these things CAN be directly converted from str -> int, so if it can, then combine current string cell with the cell to its left, then pop/remove the "full intiger" cell I just checked (i basically identify the fault, and re-append them as they should be) 
			for i in range(len(holder)):
				try: 
					fixCommaErr = int(holder[i])
					#next line of code should run if it works... allowing me to append previous thing with current, fixing the issue (and deleting the mistake from the array)
					holder[i-1] = holder[i-1] + "." + holder[i]
					print("ATTEMPT TO FIX ERROR: " + str(holder[i-1]))
     
     
     
					holder.pop(i) #remove the BAD number from array 
     
     
     
     
					#time.sleep(1) #FOR DEBUGGING ONLY
				except:
					print("Valid Cell, skipping...")
			#----Check for random "phantom-text" (Sometimes, array will make an empty instance where a string should be, but not fill it with ANY characters... Rare, but often enough to happen 1/250ish frames (from what i've tested thus far)) <-- This edge case SHOULD only happen ALSO if the array is longer than 6 items as well 
				for j in range(len(holder)):
					if len(str(holder[j])) <3: #just chose 3 cause I could, if there's less than 3 characters in there, POP the item in the array 
						holder.pop(j)

			#Edge Case - All Letters, No numbers (happened 1/355 times)
				print("HolderV2: " + str(holder))
    
				countForEdgeCase0 = len(holder) #Length of the array (before entering the while loop)
				tempCounter = 0 #a throw-away counter : used for below while loop
    
				while tempCounter != countForEdgeCase0:
					print("CHECK_FOR_ALL_CHARS: " + str(holder[tempCounter]))
					if not checkForNumbers(holder[tempCounter]): #from custom program I made in this folder 
						#holder.pop(tempCounter)
						holder[tempCounter] = 0
						print("ITEM MODIFIED!")
						countForEdgeCase0 -=1 #Since I POPED an item, I NOW need to decriment the total length of the array recorded 

					
					tempCounter += 1 #END OF WHILE LOOP 
					#if  holder[j].isnumeric() != True: #If ALL items in there are NOT numeric, KILL IT! 
						#holder.pop(j)
		
  
		#Edge case - No Text on screen to detect (if the length is too long or too short, this just fixes the issue)
		if (len(holder) != 6):# or (len(holder) >= 1): #if holder is pretty much empty 
			print("TRIGGERED!!! - This should print when there is only 1 thing in the array (no text on screen)")
		else: #-----------THIS IS THE CORE CHUNK OF THE PROGRAM THAT MAKES THE MAGIC HAPPEN 
			tempCounter = 0 #RESET BEFORE USE
			for i in holder: #make it ONLY numbers now (removes all non-numbers [keeps period])
				print(i)
				output = re.findall(r"[-+]?\d*\.\d+|\d+", i)
				holder[tempCounter] = float(output[0])
				tempCounter += 1
			print(holder)
			#print(temp)
			tempCounter = 0
	
	
			Lat.append(holder[0])
			Long.append(holder[1])
			Spd.append(holder[2])
			Bear.append(holder[3])
			Alt.append(holder[4])
			Accu.append(holder[5])

print("LAT: " + str(Lat))

#					if i == auth2[0]: #a -> La -> Latitude
#						infoBuffer[0] = text[tempCounter + 3:{NUMBER HERE FOR THE LOCATION OF THE FIRST BAR}]
#			tempCounter += 1

       #get lat
       #get lon
       #get spd
       #get bear
       #get alt
	   #get accu
  
  
  
  
  
