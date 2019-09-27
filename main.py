from PIL import Image
import exif
import glob
import os
import shutil

# path = str(input())
source_folder = str('E:/jpg/')
destination_folder = str('E:/jpg1/')

# if os.path.exists(source_folder):
#     pass
# else:
#     input(str(source_folder))
#     os.mkdir(source_folder)

if os.path.exists(destination_folder):
    pass
else:
    input(str(destination_folder))
    os.mkdir(destination_folder)

os.chdir(source_folder)

# TODO: add exif check here

for file in glob.glob('*.JPG'):
    with Image.open(file) as image:
        height, width = image.size
        file = image.resize((200, 200))
        image.save(destination_folder + file)
    shutil.copy(file, destination_folder, follow_symlinks=True)
