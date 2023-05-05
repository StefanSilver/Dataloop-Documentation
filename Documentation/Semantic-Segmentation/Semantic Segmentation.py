#!/usr/bin/env python
# coding: utf-8

# Semantic Segmentation in Dataloop's Python SDK



#importing Dataloop's Python Package and Numpy
import dtlpy as dl
import numpy as np


#Logging in to Dataloop (checks if token expired ~24h expiration time for token)
if dl.token_expired():
   dl.login()
#you can also use the simple login: 
#dl.login()



# Importing the Project and Dataset - change with your own project and dataset
project = dl.projects.get(project_name='CreatureHunt')

dataset = project.datasets.get(dataset_name='Creatures')

# Go search for your Item ID, by openinng the dataset inthe  webUI
#dataset.open_in_web()


#get the item - change the ID with your Item ID
item = dl.items.get(item_id='63eb694dbb4d84844887871d')


# Create a builder instance
builder = item.annotations.builder()
# Create polygon annotation with label
# with array of points: [[x1, y1], [x2, y2], ..., [xn, yn]]
builder.add(annotation_definition=dl.Polygon(geo=[[100, 50],
                                                  [500, 800],
                                                  [800, 50]],
                                             label='SomePoly'))

# Upload polygon to the item
item.annotations.upload(builder)


#You can check the Annotation was added to your image using this line. It should be an Polygon.
item.open_in_web()


from PIL import Image

filters = dl.Filters()
# set resource
filters.resource = 'items'

# add filter - only files

filters.add(field='type', values='file')

# add annotation filters - only Items with polygon annotations

filters.add_join(field='type', values='segment')

# get results and add them to a page

pages = dataset.items.list(filters=filters)

# loop through all Items in the page and convert the polygon to a semantic mask

for page in pages:
    for item in page:
        print('item=' + item.id)
        annotations = item.annotations.list()
        item = dataset.items.get(item_id=item.id)
        buffer = item.download(save_locally=False)
        img = Image.open(buffer)
        builder = item.annotations.builder()
        # run over all annotation in item
        for annotation in annotations:
            # print(annotation)
            if annotation.type == 'segment':
                print("Found polygon annotation - id:", annotation.id)
                builder.add(dl.Segmentation.from_polygon(geo=annotation.annotation_definition.geo,
                                                         # binary mask of the annotation
                                                         label=annotation.label,
                                                         shape=img.size[::-1]  # (h,w)
                                                         ))
                annotation.delete()
        item.annotations.upload(annotations=builder)



#update and list all annotations
annotations.update()
print(annotations)



# Open the item in web, to see the change. The Annotation should now be a Semantic Segmentation
item.open_in_web()


# ### Congrats, you just create a Semantic Segmentation Annotation in Dataloop!
