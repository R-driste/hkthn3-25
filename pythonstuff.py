#make a function that takes a photo and makes 300 white pixels below it
#then make a caption in teh 300 pixels
from PIL import Image
import os
#this is just an example of a photo (jung kook shirtless)
image1 = Image.open(r"C:\Users\BRHS-PLTW-09\Documents\Hack\ex1- Copy(2).png")
image1.show()

def add_margin(pil_img, bottom,color):
    width, height = pil_img.size
    new_height = height + bottom
    result = Image.new(pil_img.mode, (width, new_height), color)
    result.paste(pil_img)
    return result




im_new = add_margin(image1, 100,"white")
im_new.save(r"C:\Users\BRHS-PLTW-09\Documents\Hack\ex1(2).png", quality=95)
im_new.show()