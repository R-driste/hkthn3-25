#make a function that takes a photo and makes 300 white pixels below it
#then make a caption in teh 300 pixels
from PIL import Image, ImageDraw
import os
#this is just an example of a photo (jung kook shirtless)
image1 = Image.open(r"C:\Users\BRHS-PLTW-09\Documents\Hack\ex1.png")

def add_margin(pil_img, bottom,color):
    width, height = pil_img.size
    new_height = height + bottom
    result = Image.new(pil_img.mode, (width, new_height), color)
    result.paste(pil_img)
    return result

def caption(img):
    quote = input("Give a caption to your clip/image! ")
    wid, height = img.size
    x =  10
    y = (int(height)) - 100
    I1 = ImageDraw.Draw(img)
    I1.text((x,y), quote, fill=(255, 0, 0))
    return img


im_2 = add_margin(image1, 100,"white")
im_2.save(r"C:\Users\BRHS-PLTW-09\Documents\Hack\ex1.png", quality=95)
im3 = caption(im_2)
im3.show()
