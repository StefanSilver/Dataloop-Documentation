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
In this section, we will work on implementing a simple example of Semantic Segmentation in Dataloop's Python SDK.

We must first import the Python Libraries we are going to use, Numpy and dtlpy (Dataloop's Package). If you don't have dtlpy installed, [visit this installation guide](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/01_python_sdk_installation.md). 

```python
import dtlpy as dl

import numpy as np
```
Then, we have to log in to the platform, using the code below, which will open a new tab for you to log in. If you don't have an account, [learn how to make one](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/02_login_and_project_and_dataset_creation.md).
```python
#Logging in to Dataloop (checks if token expired ~24h expiration time for token)

if dl.token_expired():
   dl.login()
#you can also use the simple login: 
#dl.login()
```
We must then `Get` the Project and Dataset we are going to use.
```python
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
# to open the Dataset in web 
dataset.open_in_web()
```
A good way to find the Item ID is to `open_in_web` your Dataset, and then double-clicking your Dataset in the web UI and  clicking the Item you want to use. You will see the item ID open in the right-side of the Web-UI of Dataloop.
![image](https://user-images.githubusercontent.com/58508793/228821855-9ad287b3-d4df-45d5-9129-329715f0b2f5.png)

Make sure you have at least one Item in the dataset, otherwise upload one. After finding your Item's ID, we can get that Item in a variable, as seen below.
```python
item = dl.items.get(item_id='<item_id>')
```
Now we must create a Filter that will search for all Polygon Annotations, and then get a list of those Annotations in a variable:

```python
# Get all polygons

# Pay attantion each polygon must have different object ID 

filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION,
                    field='type',
                    values=dl.AnnotationType.POLYGON)

annotations = item.annotations.list(filters=filters)
```
We can then create a new image, filled with zeros, of the item height and width, and then convert each Polygon Annotation to Segmantation, using a `for` loop.

```python
image = np.zeros((item.height, item.width), dtype=np.uint8)

for annotation in annotations:

   # convert Polygon to Segmentation

   seg = dl.Segmentation.from_polygon(geo=annotation.geo,

                                      label=annotation.label,

                                      shape=(item.height, item.width),

                                      attributes=annotation.attributes)

```
Now, we can simply add the Segmentation to the image variable.
```python
# Add Segmentation geo to Image with the polygon object_id 
image = np.where(seg.geo == 1, annotation.object_id, image)

```
