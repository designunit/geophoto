from PIL import Image
import exif
import glob
import os
import shutil

# path = str(input())
source_folder = str(input())
destination_folder = str(input())

if os.path.exists(source_folder):
    pass
else:
    input(str(source_folder))
    os.mkdir(source_folder)

if os.path.exists(destination_folder):
    pass
else:
    input(str(destination_folder))
    os.mkdir(destination_folder)

os.chdir(source_folder)

# TODO: add exif check here

for file in glob.glob('*.JPG'):
    with Image.open(file) as original_image:
        resized_image = original_image.resize((200, 200))
        resized_image.save(destination_folder + file)
