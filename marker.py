#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium


# In[2]:


canadamap = folium.Map(location = [56.130,-106.35],zoom_start = 4)
canadamap


# In[3]:


# display a map with  red CircleMarker to Ontario center

# Ceated a Parent

ontario = folium.map.FeatureGroup()

# Append child to our parent

ontario.add_child(
    folium.CircleMarker(
      [51.25, -85.32],radius = 5,
      color = 'red', fill_color = 'Red'))
# Add  child to parent or to canadamap

canadamap.add_child(ontario)

canadamap
 



# In[4]:


# add label to our marker
folium.Marker(
  [51.25, -85.32],popup = 'Ontario').add_to(canadamap)

canadamap


# In[ ]:




