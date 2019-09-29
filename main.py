import glob
import os
import GPSC

from PIL import ExifTags
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS


# path = str(input())
# source_folder = str(input())
# destination_folder = str(input())
source_folder = "E:/jpg/"
filename = source_folder + 'yard.JPG'  # insert this if you need to work with file
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


# TODO: make function to get files' exif info
def get_exif(required_file):
    image = Image.open(required_file)
    image.verify()
    return image.getexif()


def get_geo_info(required_exif):
    if not required_exif:
        return None

    geo_info = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in required_exif:
                return None
            for (key, val) in GPSTAGS.items():
                if key in required_exif[idx]:
                    geo_info[val] = required_exif[idx][key]

    return geo_info


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


for file in glob.glob('*.JPG'):
    with Image.open(file) as original_image:
        exif = get_exif(file)
        geotags = get_geo_info(exif)

        # TODO: add recording to file and check rotating function
        if geotags:
            coordinates = GPSC.get_coordinates(geotags)
            print(coordinates)



        if 'GPSInfo' in metadata_of_original_image:
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
