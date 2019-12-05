# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:25:18 2019

@author: shreyas
"""

import pandas as pd
from tqdm import tqdm
from geopy.geocoders import Nominatim
import progressbar
from time import sleep
import json
bar = progressbar.ProgressBar(maxval=20, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

# function to get latitude and longitude from the given csv file
def getLatLong():
    
    # reading csv files
    df= pd.read_csv(r"C:\Users\shrey\Desktop\Geo\coordinates.csv")
    nom=Nominatim(user_agent="Bell",timeout=11)
    # cleaning data postal code as geocode takes only in 'B3j 2k9' format
    # But the data in csv is 'b3j2k9'
    df["postal1"]=df["Postal code"]
    df["postal1"]=df.postal1.str.slice(0,3)
    df["postal2"]=df["Postal code"].str.slice(3,7)
    df["postal"]=df["postal1"]+" "+df["postal2"]
    # Concatenating fields to form a complete address
    df["Address"]=df["Prov"]+" "+df["postal"]
    df['Coordin'] = tqdm(df['Address'].apply(nom.geocode))
    # Storing all latitudes to variable
    df["latitude"] = df['Coordin'].apply(lambda x: x.latitude if x != None else None)
     # Storing all Longitudes to variable
    df["longitude"] = df['Coordin'].apply(lambda x: x.latitude if x != None else None)
    for i in tqdm(df["latitude"]):
        print(i)
    for i in tqdm(df["longitude"]):
        print(i)
    
# Function to get coordinates from the geoJson files    
def getPoly():
    df1 = []
    data = json.load(open(r'C:\Users\shrey\Desktop\Bell\mygeodata\Videotron_LTE_150E.geojson'))
    for i in range(len(data['features'])):
        df = pd.DataFrame(data['features'][0])
        df1.append(df)
        #df['geometry'][3]
        df1
        df1[0]['geometry'][3]    
 
# By default magic word name is set to "__main__" and the status bar is started    
if __name__ =="__main__":
    bar.start()
    getLatLong()
    getPoly()
    sleep(0.1)
    bar.finish()