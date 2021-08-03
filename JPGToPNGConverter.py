import sys
import os
from PIL import Image

# grab the folder args.

in_folder = sys.argv[1]
out_folder = sys.argv[2]


# check if out_folder exists if not, create it.
dir_list = os.listdir()
if out_folder not in dir_list:
    abs_path = r"\Users\gauri\Documents\Python Development\image-processing"
    os.mkdir(f"{abs_path}\{out_folder}")

# loop through pokedesk and convert all images to PNG. and save them to new folder.

in_folder_list = os.listdir(f"./{in_folder}")


for file in in_folder_list:
    filename = file.split(".")[0]
    try:
        with Image.open(f"./{in_folder}/{file}") as img:
            img.save(f"./{out_folder}/{filename}.png", "png")
        print("done!")
    except OSError as err:
        print("cannot convert this file: ", filename)
        print(err)
