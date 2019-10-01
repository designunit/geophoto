import glob
import os
import sys

from PIL import Image

import coordlib
import image
import geojson


source_folder = sys.argv[1]
filename = source_folder + 'yard.JPG'
destination_folder = sys.argv[2]
name_of_the_geojson_file = destination_folder + "dataset.geojson"
url_base = sys.argv[3]
size = (int(sys.argv[4]), int(sys.argv[4]))

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

images = []
counter = 0

for file in glob.glob('*.JPG'):
    with Image.open(file) as original_image:
        exif = image.get_exif(file)
        geotags = image.get_geo_info(exif)
        required_rotation = image.get_orientation(file)
        if geotags:
            coordinates = coordlib.get_coordinates(geotags)
            image.rotating_the_image(source_folder, file, destination_folder, size)
            images.append({
                'id': counter,
                'url': url_base + file,
                'coordinates': coordinates,
                'value': 1
            })
            counter += 1
        else:
            pass

features = geojson.create_geojson(images)
geojson.save_json(name_of_the_geojson_file, features)
