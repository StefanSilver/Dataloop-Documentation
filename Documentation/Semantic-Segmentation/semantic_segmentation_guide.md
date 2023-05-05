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
At Dataloop, we also support Semantic Segmentation which allows you to annotate each pixel with a specific label (such as Car, Person, Pedestrian, Sky, etc.) without distinction between unique objects with the same label.

If you want to distinguish multiple objects that have the same label, we also provide you with **Instance Segmentation**. This method of annotating at pixel level, is very similar to Semantic Segmentation, but with the ability to detect distinct instances of the same class of objects, such as Car1, Car2, Person 1, Person2, etc.

Both Semantic Segmantiation and Instance Segmentation can be used in Dataloop, depending on the use case and need you have. If your use case requires Instance Segmentation, you can annotate using our powerful polygon tool which has a variety of features, and can later generate instance segmentation as an output.

This Guide will show developers how they can implement Semantic Segmentation in Dataloop's Python SDK. However, if you want to learn how to perform Semantic Segmentation on the Dataloop Web UI, we have video tutorials which will walk you through the process. [Check out our YouTube channel](https://www.youtube.com/channel/UCCvp-nw5mK9bb9lDNcD6fgw/featured) for tutorials on using Dataloop:

[![image](https://user-images.githubusercontent.com/58508793/226386974-10b9445d-5ddc-48e4-89d4-4bc17f30c61f.png)](https://dataloop.ai/video/tutorial-semantic-segmentation/)

## Python SDK Semantic Segmentation
In this section, we will work on implementing a simple example of Semantic Segmentation using Dataloop's Python SDK.

We must first import the Python Libraries we are going to use; `numpy` and `dtlpy` (Dataloop's Package). If you don't have `dtlpy` installed, [visit this installation guide](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/01_python_sdk_installation.md). 

```python
import dtlpy as dl

import numpy as np
```
Then, we have to log in to the platform using the code below which will open a new browser tab for you to log in. If you don't have an account, [learn how to make one](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/02_login_and_project_and_dataset_creation.md).
```python
#Logging in to Dataloop (checks if token expired ~24h expiration time for token)

if dl.token_expired():
   dl.login()
#you can also use the simple login: 
#dl.login()
```
We must then `Get` the Project and Dataset we are going to use.
```python
# Importing the Project and Dataset - change with your own project and dataset
project = dl.projects.get(project_name='CreatureHunt')

dataset = project.datasets.get(dataset_name='Creatures')

#Go search for your Item ID, by openinng the dataset inthe  webUI
dataset.open_in_web()
```
**Note:** To see all of the Datasets available in your Project, use `project.datasets.list()`.


A visual way to find the Item ID is to `open_in_web` your Dataset then double-click your Dataset in the web UI to open it.  Once the command is executed, a new screen will open. You must got to the pannel on the left of the screen -> Data Management -> Dataset and then click the Dataset you are using; then you can click the Item you want to use. You will see the item ID open in the right-side of the Web-UI of Dataloop.
![image](https://user-images.githubusercontent.com/58508793/228821855-9ad287b3-d4df-45d5-9129-329715f0b2f5.png)

Make sure you have at least one Item in the Dataset, otherwise upload one. After finding your Item's ID, we can set that Item ID as a variable `item`.  See below.
```python
#get the item - change the ID with your Item ID
item = dl.items.get(item_id='63eb694dbb4d84844887871d')
```
***Important!***--> If you don't have a Polygon Annotation created for your Item, you can create a basic one, using the code snippet below. It should work as it is, but if you want, you can modify the geo parameters. Also, as you will notice, this code will create both a [Polygon and a Polyline Annotation](https://developers.dataloop.ai/tutorials/annotations_image/polygon_and_polyline/chapter/).

```python

# Create a builder instance
builder = item.annotations.builder()
# Create polygon annotation with label
# with array of points: [[x1, y1], [x2, y2], ..., [xn, yn]]
builder.add(annotation_definition=dl.Polygon(geo=[[100, 50],
                                                  [80, 120],
                                                  [110, 130]],
                                             label='SomePoly'))

# Upload polygon to the item
item.annotations.upload(builder)

```
If everything goes well, you should get an output similar to this:
```python
AnnotationCollection(item=Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63e6283b4a03c631b54725ec', created_at='2023-02-14T10:58:21.000Z', dataset_id='63e6283b4a03c631b54725ec', filename='/098-696200529-scale10.00-k_euler_a-sd-v1-5-fp16.png', name='098-696200529-scale10.00-k_euler_a-sd-v1-5-fp16.png', type='file', id='63eb694dbb4d84844887871d', spec=None, creator='myfuncont@gmail.com', _description=None, annotations_count=0), annotations=[Annotation(id='642f123bb532f66d61a0972a', item_id='63eb694dbb4d84844887871d', creator='myfuncont@gmail.com', created_at='2023-04-06T18:40:59.578Z', type='segment', item_height=1024, item_width=1024, label_suggestions=None, _start_frame=0, _start_time=0), Annotation(id='642f123bb532f6f5bfa09729', item_id='63eb694dbb4d84844887871d', creator='myfuncont@gmail.com', created_at='2023-04-06T18:40:59.576Z', type='polyline', item_height=1024, item_width=1024, label_suggestions=None, _start_frame=0, _start_time=0)])
```
You can check if the Polygon Annotation was succesfully added in your Item, by opening that Item in the WebUI.
```python
#You can check the Annotation was added to your image using this line
item.open_in_web()
```
For the Annotation we just created, the Polygon should just be a big Triangle on the screen, as you can see below.

![image](https://user-images.githubusercontent.com/58508793/236408237-97b0876d-313e-435e-a72b-9965f671f39d.png)



Now we must create a Filter that will search for all Polygon Annotations on Items in the Dataset and convert those polygons to semantic masks. Just take the code below as it is (no changes required) and use it to look for all Annotations of Polygon Types and convert them into Semantic Segmentation Annotations.

```python

# From the Docs - https://sdk-docs.dataloop.ai/en/latest/tutorials/annotations_image/segmentation/chapter.html#init-segmentation

# Goes to the Dataset and gets all items then looks for all annotations of the Polygon type.  Converts all of those polygons to Semantic Masks

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
```
If you successfully run the code above, the console output should look similar to what you see below.
```python
Download Items: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  9.45it/s]
Found polygon annotation - id: 6454bd4fa55a8064d8edf0dd
Iterate Pages: 100%|█████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.71it/s]
```
And if you use `item.open_in_web()` the new Semantic Segmentation Annotation should look like this:

![image](https://user-images.githubusercontent.com/58508793/236408901-9de67ca3-301d-4c3e-98c5-e42b117f7990.png)

You have successfully converted the Polygon Annotation to a Semantic Segmentation Annotation! 


## Final Words
Semantic Segmentation can be a very useful tool. We hope this guide helped you learn how to use it as part of our platform.

We welcome you to continue your journey with Dataloop by using the following links: 

1. [Dataloop Python SDK Release Notes](https://dataloop.ai/docs/sdk-release-notes)
2. [Dataloop Platform UI Documentation](https://dataloop.ai/docs/welcome)
3. [Structured, Public, and Fully Verified to Work Dataloop GitHub Developer Community Space](https://github.com/dataloop-ai-apps)
4. [Unstructured, Public Dataloop GitHub Space](https://github.com/dataloop-ai)

If you have any questions, we encourage you to submit your question to the [Dataloop Developer Community](https://github.com/dataloop-ai-apps/dataloop-devs/discussions/new?category=q-a). One of our  Developer Success Engineers or someone from the community will help as quickly as they can.

You can also submit issues to our Support team by opening a question through the support widget located in the upper right corner of the platform UI. Our team is available to assist you with any inquiries you may have and we are happy to help!
