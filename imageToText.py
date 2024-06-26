#https://www.geeksforgeeks.org/how-to-extract-text-from-images-with-python/
#NOTE: Apparently, that tesseract.exe for a windows machine MUST be installed seporately, IN ADDITION to the python library, documentation prefers instalation be located at "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
from PIL import Image 
from pytesseract import pytesseract 

# Defining paths to tesseract.exe 
# and the image we would be using 
def imageToText(image_path, fileName ): 
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #program path that is used for Windows for the image-to-text pgm
    
    # Opening the image & storing it in an image object 
    img = Image.open(image_path + "\\" + fileName) 

    # Providing the tesseract executable 
    # location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract 

    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = pytesseract.image_to_string(img) 

    # Displaying the extracted text 
    #print(text[:-1])
    return  text[:-1]

#imageToText("C:\\Users\\nicpi\\OneDrive\\Documents\\Python_VideoToText_DroidScriptVideo_GPS\\GetGPSFromDroidScript", "demoImage.jpg")