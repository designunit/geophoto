import json


def create_geojson(images):
    return {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': img['coordinates'],
                    'properties': {
                        'url': img['url']
                    },
                }
            }
            for img in images
        ]
    }


def save_json(required_name_of_file, my_details):
    with open(required_name_of_file, "w+")as json_file:
        json.dump(my_details, json_file, indent=4)
