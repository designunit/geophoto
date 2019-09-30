import glob
import os

from PIL import Image

import coordinates_convector
import image
import geojson

# path = str(input())
# source_folder = str(input())
# destination_folder = str(input())
source_folder = "E:/jpg/"
filename = source_folder + 'yard.JPG'
destination_folder = "E:/jpg1/"
name_of_the_geojson_file = destination_folder + "coordinates_and_titles.geojson"
url_base = 'http://google.com/'

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
        exif = image.get_exif(file)
        geotags = image.get_geo_info(exif)
        required_rotation = image.get_orientation(file)
        if geotags:
            coordinates = coordinates_convector.get_coordinates(geotags)

            image.rotating_the_image(source_folder, file, destination_folder)
        else:
            pass

features = geojson.create_geojson([{
    'url': url_base + file,
    'coordinates': coordinates
}])
geojson.save_json(name_of_the_geojson_file, features)
