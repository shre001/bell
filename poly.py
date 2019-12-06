
# coding: utf-8

# In[1]:


from shapely.geometry import Point


# In[2]:


from shapely.geometry.polygon import Polygon


# In[3]:


point=Point(0.5,0.5)


# In[4]:


polygon=Polygon([(0,0),(0,1),(1,1),(1,0)])
print(polygon.contains(point))


# In[7]:


import json


# In[10]:


with open("C:\\Users\cay1kor\Desktop\Videotron_LTE_150E.geojson") as f:
    data=json.load(f)
poly_list=[]
for feature in data["features"]:
    print(feature["geometry"]["type"])
    print(feature["geometry"]["coordinates"])
    poly_list.append(feature["geometry"]["coordinates"])


# In[12]:


len(poly_list[0])


# In[19]:


sample=poly_list[0][0]


# In[21]:


polygon_1=Polygon(sample)


# In[24]:


point=Point(-77.24,48.09)


# In[25]:

#for actual file
print(polygon_l.contains(point))

