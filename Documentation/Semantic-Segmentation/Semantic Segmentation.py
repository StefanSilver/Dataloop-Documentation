#!/usr/bin/env python
# coding: utf-8

# # Semantic Segmentation in Dataloop's Python SDK
# 

# In[51]:


#importing Dataloop's Python Package and Numpy
import dtlpy as dl
import numpy as np


# In[ ]:


#Logging in to Dataloop (checks if token expired ~24h expiration time for token)
if dl.token_expired():
   dl.login()
#you can also use the simple login: 
#dl.login()


# In[ ]:





# In[52]:


# Importing the Project and Dataset - change with your own project and dataset
project = dl.projects.get(project_name='CreatureHunt')

dataset = project.datasets.get(dataset_name='Creatures')

#Go search for your Item ID, by openinng the dataset inthe  webUI
dataset.open_in_web()


# In[53]:


#get the item - change the ID with your Item ID
item = dl.items.get(item_id='63eb694dbb4d84844887871d')


# In[54]:


# Create a builder instance
builder = item.annotations.builder()
# Create polygon annotation with label
# with array of points: [[x1, y1], [x2, y2], ..., [xn, yn]]
builder.add(annotation_definition=dl.Polygon(geo=[[200, 50],
                                                  [80, 120],
                                                  [110, 130]],
                                             label='my-label'))
# (optional) create Polyline annotation with label
#builder.add(annotation_definition=dl.Polyline(geo=[[200, 50],
#                                                   [80, 120],
#                                                   [110, 130]],
#                                              label='my-label'))
# Upload polygon to the item
item.annotations.upload(builder)


# In[55]:


#You can check the Annotation was added to your image using this line
item.open_in_web()


# In[61]:


# Get all polygons

# Pay attention each polygon must have different object ID 
# Here we create a filter that will look for all Polygon Annotations
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION,
                    field='type',
                    values=dl.AnnotationType.POLYGON)
#we get a list of annotations of a specific item
annotations = item.annotations.list(filters=filters)


# In[59]:


#update and list all annotations
annotations.update()
print(annotations)


# In[84]:


# create a blank copy of the h/w size of your image Item
image = np.zeros((item.height, item.width), dtype=np.uint8)

for annotation in annotations:
    # convert Polygon to Segmentation
    seg = dl.Segmentation.from_polygon(geo=annotation.geo,

                                      label=annotation.label,

                                      shape=(item.height, item.width),

                                      attributes=annotation.attributes)


# In[85]:


# Add Segmentation geo to Image with the polygon object_id 

image = np.where(seg.geo == 1, annotation.object_id, image)

# Print the segm which should be of type = Segmantation, if everything went fine
print(seg)


# ### Congrats, you just create a Semantic Segmentation Annotation in Dataloop!
