#https://www.geeksforgeeks.org/python-pil-image-crop-method/
# Importing Image class from PIL module
from PIL import Image



def crop(filePath, fileName): 
    # Opens a image in RGB mode
    #dir = "C:\\Users\\nicpi\\OneDrive\\Documents\\Python_VideoToText_DroidScriptVideo_GPS\\demoImage.jpg"
    im = Image.open(filePath + "\\" + fileName) #frame0.jpg") #(r"C:\Users\Admin\Pictures\geeks.png")

    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = im.size

    # Setting the points for cropped image
    left = 5
    top = height / 5
    right = width*0.75 #164
    bottom = height * 0.3 #3 * height / 4

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    # Shows the image in image viewer
    #im1.show()

    im1.save(fileName)

#directory = "C:\\Users\\nicpi\\OneDrive\\Documents\\Python_VideoToText_DroidScriptVideo_GPS\\GetGPSFromDroidScript"
#fileName = "demoImage.jpg"
#crop(directory, fileName)