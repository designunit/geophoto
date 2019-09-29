import glob
import os

from PIL import Image

import coordinates_convector
import redact_functions

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

for file in glob.glob('*.JPG'):
    with Image.open(file) as original_image:
        exif = redact_functions.get_exif(file)
        geotags = redact_functions.get_geo_info(exif)
        required_rotation = redact_functions.get_orientation(file)
        # print(required_rotation)
        # TODO: add recording to file and check rotating function
        if geotags:
            coordinates = coordinates_convector.get_coordinates(geotags)
            redact_functions.rotating_the_image(source_folder, file, destination_folder)
            # print(coordinates)

            # changing_orientation_index = 'Orientation'
            # if changing_orientation_index in metadata_of_original_image:
            #     orientation_index = metadata_of_original_image['Orientation']
            #     rotation_angle = get_rotation(orientation_index)
            #     rotated_image = original_image.rotate(rotation_angle)
            #     resized_image = rotated_image.resize((200, 200))
            #     resized_image.save(destination_folder + file)
            # else:
            #     pass
        else:
            pass
