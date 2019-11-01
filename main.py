import glob
import os
import sys

from PIL import Image

import coordlib
import imglib
import geojson


source_folder = sys.argv[1]
destination_folder = sys.argv[2]
full_name_of_the_geojson_file = os.path.join(destination_folder, 'dataset.geojson')
url_base = sys.argv[3]
size = (int(sys.argv[4]), int(sys.argv[4]))

if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)
else:
    pass

images = []
counter = 0

for file in glob.glob(os.path.join(source_folder, '*.JPG')):
    file_with_normpath = os.path.normpath(file)
    image = Image.open(file_with_normpath)
    exif = imglib.get_exif(image)
    geotags = imglib.get_geo_info(exif)
    if geotags:
        coordinates = coordlib.get_coordinates(geotags)
        path = os.path.join(file, destination_folder)
        imglib.saving_img(image, path, size)

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
geojson.save_json(full_name_of_the_geojson_file, features)
