## <a name="find_item_id"></a> How to find an Item's ID
The easiest way to find an Item's ID is to actually open the Items inside of the Dataset in the WebUI of Dataloop. To do that, run the code below:
```python
d_set.items.open_in_web()
```
This will open the WebUI of Dataloop, which will show all of the Items you have inside of the Dataset. By clicking one of the Items, you will see its ID. You can see that visually in the image below - the Item ID and Dataset ID are highlighted:
![image](https://github.com/StefanSilver/Dataloop-Documentation/assets/58508793/278938d3-9a96-4744-8435-42c2061640b5)









## <a name="open_in_web"></a> dl.items.open_in_web()
The `dl.items.open_in_web()` method allows you to open the Item of your choosing in the WebUI of Dataloop.

You can see all of the details of this function, below.

### open_in_web()

**Definition:** `open_in_web(filepath=None, item_id=None, item=None)`

***Opens the Item in the Web platform.***

**Prerequisites:** You must be in the role of an Owner or developer or be an Annotation Manager/Annotator with access to that Item through Task.

**param str filepath**
- item file path

**param str item_id**
- item id

**param dtlpy.entities.item.Item item**
- item entity

**Example:**
```python
dataset.items.open_in_web(item_id='item_id')
#or
item_variable.open_in_web()
```

In our case, let's open item1 in web:
```python
item1.open_in_web()
```
This will open your Item in a new tab:
![image](https://github.com/StefanSilver/Dataloop-Documentation/assets/58508793/f9c16b9c-88d5-4c21-a813-b0500e89cd67)

