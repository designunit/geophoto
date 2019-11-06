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
### Syntax:
```
$ python3 geophoto.py <source_folder_path> <output_folder_path> <link> <size>
```
1) ```<source_folder_path>``` - is your folder with jpeg images
2) ```<output_folder_path>``` - is your folder which you want to contain output data
3) ```<link>``` - is link which contains every image address
4) ```<size>``` - is size of output images in output folder 
### Example:
In ```<source_folder_path>``` and ```<output_folder_path>``` do not forget to use full name of folders with which you interact, as in example below:
```
$ python3 geophoto.py /home/usr/source_folder/ /home/usr/output_folder/ google.com 200
```
Make sure to run this program in downloaded project directory, otherwise it won't work.
