# Geophoto

## What this software does:
1) Takes folder which contains huge amount of jpeg images
2) Takes every image in order which contains geodata, images that do not contain geodata will be skipped
3) Writes geodata to 'dataset.geojson' file, it will be automatically generated in ```<output_folder_path>```
4) Resizes chosen images and saves them to ```<output_folder_path>```, this is made for preview purposes
5) As a result you will have ```<output_folder_path>```, which contains all info you needed

### Run
```
$ python3 geophoto.py <source_folder_path> <output_folder_path> <link> <size>
```

Be sure to run this program in project directory, otherwise it won't work.

In ```<source_folder_path>``` and ```<output_folder_path>``` do not forget to use full name of folders with which you interact.
