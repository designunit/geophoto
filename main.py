import glob
import os

from PIL import ExifTags
from PIL import Image

# path = str(input())
# source_folder = str(input())
# destination_folder = str(input())
source_folder = "E:/jpg/"
destination_folder = "E:/jpg1/"
name_of_the_geojson_file = "coordinates.geojson"

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

# TODO: get the right arguments
def get_rotation(orientation):
    if orientation == 1:
        pass
    if orientation == 2:
        return -90
    if orientation == 3:
        return -90
    if orientation == 4:
        return -90
    if orientation == 5:
        return -90
    if orientation == 6:
        return -90
    if orientation == 7:
        return -90
    if orientation == 8:
        return -90
    return 0

# TODO:
# def get_record(arg0, arg1):



# TODO: add exif check here
for file in glob.glob('*.JPG'):
    with Image.open(file) as original_image:
        # TODO: checking the desired file
        metadata_of_original_image = {
            ExifTags.TAGS[k]: v
            for k, v in original_image.getexif().items()
            if k in ExifTags.TAGS
        }
        if 'GPSInfo' in metadata_of_original_image:  # CHECKED AVAILABILITY OF GPS COORDINATES; NEED TO RESIZE IT NOW
            # TODO: WRITE COORDINATES HERE IN GEOJSON FILE
            my_file = open(destination_folder + name_of_the_geojson_file, "w+")
            if 'Latitude:' in metadata_of_original_image:
                my_file.write("Latitude:" + metadata_of_original_image['GPSInfo'])
            elif 'Longitude:' in metadata_of_original_image:
                my_file.write("Longitude:" + metadata_of_original_image['GPSInfo'])

            changing_orientation_index = 'Orientation'
            if changing_orientation_index in metadata_of_original_image:
                orientation_index = metadata_of_original_image['Orientation']
                rotation_angle = get_rotation(orientation_index)
                rotated_image = original_image.rotate(rotation_angle)
                resized_image = rotated_image.resize((200, 200))
                resized_image.save(destination_folder + file)
            else:
                pass
        else:
            pass
