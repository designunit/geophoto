import PIL

from PIL import ExifTags
from PIL import Image
from PIL import ImageOps
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS


def get_exif(required_img):
    required_img.verify()
    return required_img.getexif()


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


def get_orientation(required_img):
    with Image.open(required_img) as required_image:
        metadata_of_original_image = {
            ExifTags.TAGS[k]: v
            for k, v in required_image.getexif().items()
            if k in ExifTags.TAGS
        }
        if 'Orientation' in metadata_of_original_image:
            orientation_index = metadata_of_original_image['Orientation']
            return orientation_index
        elif 'Orientation' not in metadata_of_original_image:
            return None


def get_rotate(orientation):
    if orientation == 1:
        return 0
    elif orientation == 3:
        return 180
    elif orientation == 6:
        return 270
    elif orientation == 8:
        return 90
    return 0


def operations_run1(required_img, saving_path, img_size):
    image_obj = Image.open(required_img)
    orientation = get_orientation(required_img)
    degrees = get_rotate(orientation)
    rotated_image = image_obj.rotate(degrees)
    resized_image = PIL.ImageOps.fit(rotated_image, img_size, centering=(0.5, 0.5))
    resized_image.save(saving_path + required_img)
