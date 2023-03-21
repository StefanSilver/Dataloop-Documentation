# Semantic Segmentation

## What is Semantic Segmentation?
Semantic segmentation is a computer vision technique that involves dividing an image into meaningful parts or regions, known as segments, and labeling each segment with a corresponding class label. This technique is used in a wide range of applications, including autonomous driving, medical image analysis, and object recognition.

In semantic segmentation, the goal is to identify and differentiate between different objects or parts of an image. This is achieved by assigning each pixel in the image to a specific category or class. 

Semantic segmentation has numerous applications in computer vision, including autonomous driving, where it is used to detect and classify objects on the road, such as cars, pedestrians, and traffic signs. It is also used in medical image analysis, where it can be used to identify and segment different types of tissue in MRI or CT scans.

Semantic segmentation is different compared to other image based tasks, as you can see below:

- Image Classification - identifies a single class that is assigned to the whole image.
- Object Recognition - identifies what is present in the image and where using a Bounding Box (a rectangle); this envelops an item from an image, but also pixels that are not part of that item (due to the rectangular Bounding Box).
- Semantic Segmentation - identifies ***precisely*** what is present in the image and where, by finding all pixels that belong to a specific item in the image.

Semantic segmentation is a powerful computer vision technique that allows you to identify and classify different objects and parts of an image with increased precission copared to other methods. With advances in deep learning and neural network architectures, semantic segmentation is becoming increasingly accurate and reliable, making it an essential tool for a wide range of applications.

## Dataloop's Semantic Segmentation
At Dataloop, we also support Semantic Segmentation, which allows you to annotate each pixel with a specific label (such as Car, Person, Pedestrian, Sky, etc.) without distinction between unique objects with the same label.

If you want to distinguish multiple objects that have the same label, we also provide you with **Instance Segmentation**. This method of annotating at pixel level, is very similar to Semantic Segmentation, but with the ability to detect distinct instances of the same class of objects, such as Car1, Car2, Person 1, Person2, etc.

Both Semantic Segmantiation and Instance Segmentation can be used in Dataloop, depending on the use case and need you have. If your use case requires Instance Segmentation, you can annotate using our powerful polygon tool which has a variety of features, and can later generate instance segmentation as an output.

This Guide will show developers how they can implement Semantic Segmentation in Dataloop's Python SDK. However, if you want to learn how to perform Semantic Segmentation on the web-version of Dataloop, we have video tutorials which will walk you through the process. Remember to also [check out our YouTube channel](https://www.youtube.com/channel/UCCvp-nw5mK9bb9lDNcD6fgw/featured), for more tutorials on using Dataloop:

[![image](https://user-images.githubusercontent.com/58508793/226386974-10b9445d-5ddc-48e4-89d4-4bc17f30c61f.png)](https://dataloop.ai/video/tutorial-semantic-segmentation/)

## Python SDK Semantic Segmentation
```python
import dtlpy as dl

import numpy as np

item = dl.items.get(item_id='ITEM ID')

# Get all polygons

# Pay attantion each polygon must have different object ID 

filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION,
                    field='type',
                    values=dl.AnnotationType.POLYGON)

annotations = item.annotations.list(filters=filters)

image = np.zeros((item.height, item.width), dtype=np.uint8)

for annotation in annotations:

   # convert Polygon to Segmentation

   seg = dl.Segmentation.from_polygon(geo=annotation.geo,

                                      label=annotation.label,

                                      shape=(item.height, item.width),

                                      attributes=annotation.attributes)

# Add Segmentation geo to Image with the polygon object_id 
image = np.where(seg.geo == 1, annotation.object_id, image)

```
