import csv
from pprint import pprint
import json
import os

def create_json():
    Location = []
    with open(os.getenv('DATA_DIR')+'/raw/schools.csv', 'r') as text:
        next(text)
        for line in text:
            fields = line.split(',')
            name=fields[0].strip('"')
            coordinates=fields[-1][7:-2].split()
            Location.append(
                {
                    "name" : name,
                    "longlat" : coordinates
                }
            )
    with open (os.getenv('DATA_DIR')+'/processed/format_schools.json', 'w') as outfile:
        outfile.write(json.dumps(Location))
