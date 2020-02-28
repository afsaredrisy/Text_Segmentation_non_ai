## Text Segmentation from an image with Binarization

This repository contains a simple solution to separate text from background. Solution is using simple binarization it may not work for all kinds of images.
Repository contains one python file `get_text_overlayed.py` to run the project execute following line from your cli.


**Python 3**
```bash

python3 get_text_overlayed.py

```


**Python**
```bash

python3 get_text_overlayed.py

```

Once you run the script output of the program will be save to output_image directory. 
Here is main logic.

```python
def getTextOverlay(input_image): 
    # Here is my simple implementation
    gray = input_image.convert("L")
    output = gray.point(lambda pixel: 0 if pixel<6 else 255)
    
    return output
```

# Requirement

Only Python is required nothing else (No need to install OpenCV to run this script)



# Conclution 
 Note: This solution will not work for all images to segment text if we want to segment text from all kinds of images then we need to train  our own CNN model.
