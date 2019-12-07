# bell
## Author
Shreyas Bhaktavatsala

## IDE
Anacondo Jupiter Notebook 

## Python Version
Python 3.7.4 stable release

#Libraries used
Pandas- datafrmes
tqdm- to add time elpased and staus
progressbar- to add progressbar
geopy - to get lat and long
json - to read json file
## Day1 Learning
Some of the learning for today were:

1. Analyzed the given Excel sheet and figured out the only way to get lat and long was from the address given.
2.Discovered the libraries available in python and learnt about geocode and reverse geocode.
3. Came across geopy library that has several geocoders. Chose Nominatim module to suit my needs for this problem statement.
4. Found inconsistency in the given address as geocode took data in specific format. Ex: Postal B3j2k9 was not accepting. Instead B3j 2k9 was a good parameter. Hence data cleaning was necessary.
5.Found a way to add status bar using progressbar and tqdm modules.
6. extracted mapInfo file geoJson 
7. extracted coordinates in the Json file  using json reader.

## Day2 Learning

1. Analyzed the given GEOJSON file and had a look into GEOJSON format
2. Learnt about Feature, FeatureCollection and type of geometries (points, linestring,multipolygon,polygon). Points and polygon are the geometries of our concern
3. Understood that our GEOJSON  has type polygon with holes. There are 13 polygons with 11 of them having holes in them.
4. Designed a logic to cut the interiors( coordinates of the holes) from our exterior( the outer boundary of our polygon)
5. Used library to read our geojon file
6. iterated and stored the polygons in terms of list to feed as input to the imported shapely library.
7. Exploring geopand and geopanda dataframes.

## Day3
365 coordinates lying inside the given 13 polygons
