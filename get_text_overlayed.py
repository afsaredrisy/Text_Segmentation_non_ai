# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
from PIL import Image


def getTextOverlay(input_image): 
    # Here is my simple implementation
    gray = input_image.convert("L")
    output = gray.point(lambda pixel: 0 if pixel<6 else 255)
    
    return output

if __name__ == '__main__':
    image = Image.open('input_image/simpsons_frame0.png')
    output = getTextOverlay(image)
    output.save('output_image/simpons_text.png')
