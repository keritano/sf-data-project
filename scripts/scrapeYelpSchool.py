from yelpapi import YelpAPI
import os
from pprint import pprint
import json
import time
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
from geopandas import GeoDataFrame


api_key=os.getenv('API_KEY')

yelp_api = YelpAPI(api_key, timeout_s=3.0)

with open('format_schools.json') as json_file:
    data = json.load(json_file)
school_info = []
for entry in data:
	name = entry['name']
	longitude= float(entry['longlat'][0])
	latitude = float(entry['longlat'][1])
	response = yelp_api.autocomplete_query(text=name, latitude=latitude, longitude=longitude)
	for biz in response['businesses']:
		school_info.append(
			{
			"latitude":latitude,
			"longitude":longitude,
			"id":biz['id'],
			"name":name,
			}
		)
		break
	break
for school in school_info:
	response = yelp_api.business_query(id=school['id'])
	school['rating']=response['rating']
	school['name']=response['name']

df = pd.DataFrame(school_info)
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
usa = gpd.read_file('./bayarea_zipcodes.shp')
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);
input('a')