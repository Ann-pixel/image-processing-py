from PIL import Image, ImageFilter

pika = Image.open("./pokedesk/pikachu.jpg")
# print(pika.size, pika.format, pika.mode)
# print(
#     dir(pika)
# )  # python way to get a list of all methods and attributes on an instance.

# filtered_pika1 = pika.filter(ImageFilter.BLUR())
# filtered_pika1.save("./processed/blurred-pika.png", "png")

# filtered_pika2 = pika.filter(ImageFilter.SMOOTH())
# filtered_pika2.save("./processed/smooth-pika.png", "png")

# filtered_pika3 = pika.filter(ImageFilter.SHARPEN())
# filtered_pika3.save(
#     "./processed/sharp-pika.png", "png"
# )  # png supports these image filters.

# filtered_pika4 = pika.convert("L")  # greyscale
# filtered_pika4.save("./processed/grey-pika.png", "png")

# filtered_pika4.show()  # opens the image in Photos app. other image app on your mc.

# crooked_pika = pika.rotate(90)
# crooked_pika.save("./processed/rotate-pika.png", "png")

# resized_pika = pika.resize((300, 300))  # accepts a tuple
# resized_pika.save("./processed/resized-pika.png", "png")


# cropped_pika = pika.crop((100, 100, 400, 400))  # a 300x300 box.
# cropped_pika.save("./processed/cropped-pika.png", "png")


lake_img = Image.open("./images/lake-mi.jpeg")
# print(lake_img.size)
# # resize does not keep its aspect ratio.
# # use thumbnail instead.
# resized_lake_img = lake_img.resize((400, 200))
# resized_lake_img.save("./processed/resize_lake_img.jpg")


# tries to maintain the aspect ratio still.. so actual size may be something like 400,380 or something
# lake_img.thumbnail((400, 400))  # thumbnail changes on the lake_img instance in place.
# lake_img.save("./processed/thumbnail_lake_img.jpg")
