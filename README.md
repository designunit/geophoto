# Geophoto

## What does this software do:
1) Takes folder which contains huge amount of jpeg images - ```<source_folder_path>```
2) Takes every image in order which contains geodata, images that do not contain geodata will be skipped
3) Writes geodata to 'dataset.geojson' file, it will be automatically generated in ```<output_folder_path>``` directory
4) Resizes chosen images, depending on the value you gave it in ```<size>``` parameter and saves them to ```<output_folder_path>```, this is made for comfortable preview purposes
5) As a result you will have: ```<output_folder_path>```, which contains all required photos and .geojson file with metadata

### Install:
pip package manager is not available for this project yet, so you need to clone this repository:
```
$ git clone git@github.com:designunit/geophoto.git
```
### Usage:

Basic:
```
$ python3 geophoto.py -d SOURCE_DIR -o OUTPUT_DIR 
```

Common:
```
$ python3 geophoto.py -d SOURCE_DIR -o OUTPUT_DIR [--size THUMBNAIL_SIZE] [--thumbnail THUMBNAIL_FIELD] [--url-base URL_BASE] [--default-coord DEFAULT_COORD]
```

You can optionally setup GPS coordinates for images without EXIF data:
```
$ python3 geophoto.py -d SOURCE_DIR -o OUTPUT_DIR [--default-coord DEFAULT_COORD]
```

Help:
```
$ python3 geophoto.py -h
```

Make sure to run this program in downloaded project directory, otherwise it won't work.

