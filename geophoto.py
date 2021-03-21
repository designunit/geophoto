import os
import sys
import json
from argparse import ArgumentParser
from shutil import copy
from pathlib import Path
from tqdm import tqdm
from PIL import Image

import coordlib
import imglib


def iterate_files(source_folder, extensions):
    for file in os.listdir(source_folder):
        basename, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext in extensions:
            yield Path(file)


def img_factory(img):
    return {
        "type": "Feature",
        "id": img["id"],
        "geometry": {
            "type": "Point",
            "coordinates": img["coordinates"],
        },
        "properties": {
            "src": str(img["src"]),
            "url": str(img["url"]),
            "value": img["value"],
        },
    }


def create_geojson(images):
    return {
        "type": "FeatureCollection",
        "features": [
            img_factory(img)
            for img in images
        ],
    }


def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        required=True,
        dest="source_dir",
        type=str,
        help="path to folder with images",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        dest="output_dir",
        type=str,
        help="path to output folder",
    )
    # parser.add_argument('-o', '--output', default='dataset.geojson', dest='output', type=str, help='name of output file')
    parser.add_argument(
        "--size",
        default=100,
        dest="thumbnail_size",
        type=int,
        help="size of thumbnail in px",
    )
    parser.add_argument(
        "--thumbnail",
        default="thumbnail",
        dest="thumbnail_field",
        type=str,
        help="field name for thumbnail",
    )
    parser.add_argument(
        "--url-base",
        default="",
        dest="url_base",
        type=str,
        help="url base for thumbnail",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    source_folder = Path(args.source_dir).expanduser()
    destination_folder = Path(args.output_dir).expanduser()

    url_base = args.url_base
    size = (args.thumbnail_size, args.thumbnail_size)

    if not destination_folder.is_dir():
        os.mkdir(destination_folder)

    images = []
    counter = 0

    files = list(iterate_files(source_folder, [".jpg", ".jpeg"]))
    for file in tqdm(files):
        filepath = source_folder / file
        image = Image.open(filepath)
        image.load()
        exif = imglib.get_exif(image)
        geotags = imglib.get_geo_info(exif)
        if not geotags:
            continue
        coordinates = coordlib.get_coordinates(geotags)
        name = Path(f"{file.stem}-thumbnail.jpg")
        path = os.path.join(destination_folder, name)
        img = imglib.process_image(image, size)
        img.save(path)
        copy(filepath, destination_folder / file)
        images.append(
            {
                "id": counter,
                "url": url_base + str(name),
                "src": url_base + str(file),
                "coordinates": coordinates,
                "value": 1,
            }
        )
        counter += 1

    features = create_geojson(images)
    filename = destination_folder / Path("data.geojson")
    with open(filename, "w") as f:
        json.dump(features, f, indent=4)
