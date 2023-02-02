from polaroid_photo_square import *
from polaroid_photo_horizontal import *

from PIL import Image, ImageOps
import os

pathIn = r'C:\Users\Gleb\PycharmProjects\Polaroid_Photo\images'
pathOut = r'C:\Users\Gleb\PycharmProjects\Polaroid_Photo\editedImages'

def pick_photo_format(img):
    k = 16/9
    if img.width/img.height >= k:
        return 1
    return 2

for filename in os.listdir(pathIn):
    img = Image.open(f"{pathIn}/{filename}")
    img = ImageOps.exif_transpose(img)
    my_photo = None

    if pick_photo_format(img) == 1:
        my_photo = Polaroid_Photo_Horizontal(img,filename)
    else:
        my_photo = Polaroid_Photo_Square(img,filename)

    my_photo.save_image(pathOut)
