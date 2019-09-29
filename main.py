import glob
import os

from PIL import Image

import coordinates_convector
import redact_functions

# path = str(input())
# source_folder = str(input())
# destination_folder = str(input())
source_folder = "E:/jpg/"
filename = source_folder + 'yard.JPG'
destination_folder = "E:/jpg1/"
name_of_the_geojson_file = destination_folder + "coordinates_and_titles.geojson"

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
        if geotags:
            coordinates = coordinates_convector.get_coordinates(geotags)
            redact_functions.writing_data(name_of_the_geojson_file, coordinates, file)
            redact_functions.rotating_the_image(source_folder, file, destination_folder)
        else:
            pass
