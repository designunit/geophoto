# Geophoto

## What does this software do:
1) Takes folder which contains huge amount of jpeg images
2) Takes every image in order which contains geodata, images that do not contain geodata will be skipped
3) Writes geodata to 'dataset.geojson' file, it will be automatically generated in ```<output_folder_path>```
4) Resizes chosen images and saves them to ```<output_folder_path>```, this is made for preview purposes
5) As a result you will have ```<output_folder_path>```, which contains all info you needed

### Install:
pip package manager is not available for this project yet, so you need to clone repository:
```
$ git clone git@github.com:designunit/geophoto.git
```
### Syntax:
```
$ python3 geophoto.py <source_folder_path> <output_folder_path> <link> <size>
```
### Example:
Be sure to run this program in downloaded project directory, otherwise it won't work.
In ```<source_folder_path>``` and ```<output_folder_path>``` do not forget to use full name of folders with which you interact.
```
$ python3 geophoto.py /home/modernpacifist/Documents/jpg/ /home/modernpacifist/Documents/jpg1/ google.com 200
```
