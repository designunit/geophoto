import glob
import os
import sys

from PIL import Image

import coordlib
import imglib
import geojson

def image_files(source_folder, extensions):
    for file in os.listdir(source_folder):
        basename, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext in extensions:
            yield file

def main():
    source_folder = os.path.expanduser(sys.argv[1])
    destination_folder = os.path.expanduser(sys.argv[2])
    full_name_of_the_geojson_file = os.path.join(destination_folder, 'dataset.geojson')
    url_base = sys.argv[3]
    size = (int(sys.argv[4]), int(sys.argv[4]))

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    images = []
    counter = 0

    for file in image_files(source_folder, ['.jpg', 'jpeg']):
#    for file in os.listdir(source_folder):
#        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            image = Image.open(os.path.join(source_folder, file))
            image.load()
            exif = imglib.get_exif(image)
            geotags = imglib.get_geo_info(exif)
            if geotags:
                coordinates = coordlib.get_coordinates(geotags)
                path = os.path.join(destination_folder, os.path.basename(file))
                imglib.process_image(image, path, size)

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


if __name__ == '__main__':
    main()
