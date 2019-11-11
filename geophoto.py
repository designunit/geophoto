import glob
import os
import sys

from PIL import Image

import coordlib
import imglib
import geojson


def main():
    source_folder = sys.argv[1]
    source_folder_expanded = os.path.expanduser(source_folder)
    destination_folder = sys.argv[2]
    destination_folder_expanded = os.path.expanduser(destination_folder)
    full_name_of_the_geojson_file = os.path.join(destination_folder_expanded, 'dataset.geojson')
    url_base = sys.argv[3]
    size = (int(sys.argv[4]), int(sys.argv[4]))

    if not os.path.exists(destination_folder_expanded):
        os.mkdir(destination_folder_expanded)

    images = []
    counter = 0

    for file in glob.glob(os.path.join(source_folder_expanded, '*.JPG')):
        image = Image.open(file)
        image.load()
        exif = imglib.get_exif(image)
        geotags = imglib.get_geo_info(exif)
        if geotags:
            coordinates = coordlib.get_coordinates(geotags)
            path = os.path.join(destination_folder_expanded, os.path.basename(file))
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
