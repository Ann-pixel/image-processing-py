# import sys
import os
from PIL import Image


in_folder = "images"
out_folder = "converted_images"

images_list = os.listdir(f"./{in_folder}")
# print(images_list)

abs_path = r"\Users\gauri\Documents\Python Development\image-processing"
os.mkdir(f"{abs_path}\{out_folder}")

for img in images_list:
    filename = img.split(".")[0]
    try:
        with Image.open(f"./{in_folder}/{img}") as pic_file:
            converted_file = pic_file.convert("L")
            converted_file.save(f"./{out_folder}/{filename}.png", "png")
    except Exception as e:
        print("there was an error: ", e)
