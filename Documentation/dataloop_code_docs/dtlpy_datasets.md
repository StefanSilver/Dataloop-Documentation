# dtlpy.datasets
In this guide, we will describe how to use each method in the `dtlpy.datasets` and show how to use and what output you should get, so you can know everything about each function by the end of this section.

## Import dtlpy and log in to Dataloop
Before you do any operations on any Dataloop entity, you need to log in and import the `dtlpy` package.

```python
import dtlpy as dl
dl.setenv('prod')
#Logging in to Dataloop (checks if token expired ~24h expiration time for token)
if dl.token_expired():
   dl.login()
#you can also use the simple login: 
#dl.login()
```
---------------------------------------------
## Select Project
To work with Datasets, you must first select a Project to which you will add your Dataset. For that purpose, let's create a new Project. You can do that using:
```python
dl.projects.create(project_name='Dataset_Project')
proj = dl.projects.get(project_name='Dataset_Project')
# or created and directly get the Project inside of a variable
# proj = dl.projects.create(project_name='Dataset_Project')
```
And you can then print the details of the new Project you just created:
```python
print(proj)
```
The output should look similar to this:
```python
Project(created_at=1683805649832, creator='email@gmail.com', id='b9ee960e-9626-46c7-92d9-95c84d6a2730', name='Dataset_Project', feature_constraints=[{'name': 'downloadJsons', 'quota': 1, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 1, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 1, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 1, 'title': 'Create Driver'}])
```
---------------------------------------------
## <a name="create"></a> dl.datasets.create()
The `dl.datasets.create()` method allows you to create a new Dataset in the Project that  you are currently working on.

You can see all of the details of this function, below.

### create()

**Definition:**  `create(dataset_name: str, labels=None, attributes=None, ontology_ids=None, driver: entities.Driver=None, driver_id: str=None, checkout: bool=False, expiration_options: entities.ExpirationOptions=None, index_driver: entities.IndexDriver=None, recipe_id: str=None) -> entities.Dataset`

***Creates a new Dataset in the current Project.***

**Prerequisites:** You must be in the role of an Owner or Developer (engineer).

**param str dataset_name**
- The Name of the Dataset

**param list labels**
- Dictionary of {tag: color} or list of Label entities

**param list attributes**
- The Dataset's Ontology's attributes

**param list ontology_ids**
- (optional) The Dataset's Ontology

**param dtlpy.entities.driver.Driver driver**
- (optional) Storage driver, driver object or driver name

**param str driver_id**
- (optional) The Driver's ID

**param bool checkout**
- Sets the Dataset as a default Dataset object (cookies)

**param ExpirationOptions expiration_options**
- dl.ExpirationOptions object that contain definitions for the Dataset like MaxItemDays

**param str index_driver**
- dl.IndexDriver, Dataset driver's version

**param str recipe_id**
- (optional) The Recipe's ID

**return**
- Dataset object

**rtype**
- dtlpy.entities.dataset.Dataset

**Simple Creation Example:**
```python
project.datasets.create(dataset_name='dataset_name')
```
We will create a new dataset called `Test_Dataset` using the code above:
```python
dl.datasets.create(dataset_name='Test_Dataset')
```
Once you run that command, you should see an output that is similar to this:
```python
ataset(id='645cee1b05c36859784c0b37', url='https://gate.dataloop.ai/api/v1/datasets/645cee1b05c36859784c0b37', name='Test_Dataset', creator='email@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2023-05-11T13:31:07.545Z')
```
---------------------------------------------
## <a name="get"></a> dl.datasets.get()
The `dl.datasets.get()` method allows you to retrieve the Dataset from Datalopp's platform, inside your working code, or inside of a variable.

You can see all of the details about this method below.

### get()

**Definition:** `get(dataset_name: str=None, dataset_id: str=None, checkout: bool=False, fetch: bool=None) -> entities.Dataset`

***Retrieves a Dataset by Name or ID.***

**Prerequisites:** You must be an Owner or Developer to use this method. **You must provide at least ONE of the following params: `dataset_id` or `dataset_name`.**

**param str dataset_name**
- (optional) search by Name

**param str dataset_id**
- (optional) search by Id

**param bool checkout**
- Sets the Dataset as a default Dataset object (cookies)

**param bool fetch**
- (optional) Fetch entity from platform (True); bydefault taken from cookie

**return**
- Dataset object

**rtype**
- dtlpy.entities.dataset.Dataset

**Example:**
```python
dataset = dl.datasets.get(dataset_id='dataset_id')
#or
dataset= dl.dataset.get(dataset_name='dataset_name')

```
**Note:** We can also get the dataset directly from the Project entity (`proj`) that we created above (in this case, you need to `get()` the Project in a variable first). The code would look like this:
```python
dataset = proj.datasets.get(dataset_id='dataset_id')
#or
dataset= proj.dataset.get(dataset_name='dataset_name')
```


We will create a variable called `d_set` to avoid any confusion, and we will retrieve the Dataset we created, called `Test_Dataset` in it, using:
```python
d_set = dl.datasets.get(dataset_name='Test_Dataset')
```
We can then print the details of the `d_set` variable, to see that we retrieved the Dataset we wanted to:
```python
print(d_set)
```
The output should look like this:
```python
Dataset(id='645cee1b05c36859784c0b37', url='https://gate.dataloop.ai/api/v1/datasets/645cee1b05c36859784c0b37', name='Test_Dataset', creator='myfuncont@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2023-05-11T13:31:07.545Z')
```
----------------------------------------------
## <a name="clone"></a> dl.datasets.clone()
The `dl.datasets.clone()` method allows you to clone a Dataset, so you can keep your original untouched and work on the clone without fear of breaking anything. This can also be used for Versioning, which allows you to make changes and create checkpoints for your Dataset.

**Important!** The new Dataset will have the same Recipe and Ontology as the Original. [Read more about Recipes and Ontology](https://dataloop.ai/docs/taxonomy-overview), since they are critical building blocks of Datasets.

You can find all the details about this method below.

### clone

**Definition:** `clone(dataset_id: str, clone_name: str, filters: entities.Filters=None, with_items_annotations: bool=True, with_metadata: bool=True, with_task_annotations_status: bool=True)`

***Clones an existing Dataset.*** [Read more about cloning datatsets here](https://dataloop.ai/docs/clone-merge-dataset). 

**Prerequisites:** You must have the role of  Owner or Developer (engineer).

**param str dataset_id**
id of the dataset you wish to clone

**param str clone_name**
new dataset name

**param dtlpy.entities.filters.Filters filters**
Filters entity or a query dict

**param bool with_items_annotations**
true to clone with items annotations

**param bool with_metadata**
true to clone with metadata

**param bool with_task_annotations_status**
true to clone with task annotations' status

**return**
dataset object

**rtype**
dtlpy.entities.dataset.Dataset

**Example:**
```python
dataset_clone = proj.datasets.clone(dataset_id='dataset_id',
                      clone_name='dataset_clone_name',
                      with_metadata=True,
                      with_items_annotations=False,
                      with_task_annotations_status=False)
```
If we run that code on the existing Dataset we created `Test_Dataset`(you cane find the ID by running `d_set`), it will look like this:
```python

dataset_clone = proj.datasets.clone(dataset_id='645cee1b05c36859784c0b37',
                      clone_name='Test_Dataset_Clone',
                      with_metadata=True,
                      with_items_annotations=False,#True if you want
                      with_task_annotations_status=False)#True if you want
```
You should get a progress bar as an output. Wait untill it is completed for the clone to be created successfully:
```python
Command Progress: 100%|█████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 288.04it/s]
```
After that, you can check if the Clone was created, by printing the `dataset_clone` variable which should contain the cloned Dataset Object:
```python
print(dataset_clone) #print the cloned Dataset's details
```
The printed details should look similar to this:

```python
Dataset(id='645e3b5597a22fe0971aa231', url='https://gate.dataloop.ai/api/v1/datasets/645e3b5597a22fe0971aa231', name='Test_Dataset_Clone', creator='email@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2023-05-12T13:12:53.211Z')
```
----------------------------------------------
## <a name="delete"></a> dl.datasets.delete()
The `dl.datasets.delete()` method allows you to permanently delete a Dataset from the Dataloop Platform. Make sure that you really want to remove the Dataset and all of its contents, as **the removal is permanent**.

All of of the details about this method can be seen below.

### delete()

**Definition:** `delete(dataset_name: str=None, dataset_id: str=None, sure: bool=False, really: bool=False)`

***Deletes a Dataset forever!***

**Prerequisites:** You must be an Owner to use this method.


**param str dataset_name**
- (optional) Search by name

**param str dataset_id**
- (optional) Search by ID

**param bool sure**
- Are you sure you want to delete?

**param bool really**
- Really really sure that you are sure?

**return**
- True is success; are you sure you want success?

**rtype**
- bool

**Example:**
```python
proj.datasets.delete(dataset_id='dataset_id', sure=True, really=True) # Are you sure you are sure?
# or you can use with both name and id
# dl.datasets.delete(dataset_name='Test_Dataset_Clone', sure=True, really=True) 
```
For the purpose of showing how the `delete()` method works, we will delete the clone Dataset we created [above](#clone), called `Test_Dataset_Clone`:
```python
dl.datasets.delete(dataset_name='Test_Dataset_Clone', sure=True, really=True)
```
To this, you should get a simple output:
```python
True
```
**Note:** If the Dataset you want to delete is not in the current project you are working on, you **need** to use the `dl.datasets.delete(dataset_name='Test_Dataset_Clone', sure=True, really=True)`, as this option will look thorugh all of the Datasets you have in the current active Organization, on all Projects. 
***Important!***   We highly recommend that you delete a Dataset using its `ID`, as each ID is unique. This will always make sure that you delete the right ID. You can find the ID of all Datasets in the [WebUI version of Dataloop](https://dataloop.ai/) or by using `dl.datasets.list()` - in the current active Project. Just to make sure you know, an example of the command to delete by ID can be seen below:
```python
dl.datasets.delete(dataset_id='645e3b5597a22fe0971aa231', sure=True, really=True)
```
---------------------------------------------
## <a name="directory_tree"></a> dl.datasets.directory_tree()
The `dl.datasets.directory_tree()` method allows you find out what your Dataset's location is in Dataloop's platform, and other details regarding your Dataset.

You can find all the details about this method below.


### directory_tree()
**Definition:** `directory_tree(dataset: entities.Dataset=None, dataset_name: str=None, dataset_id: str=None)`

***Gets a Dataset's directory tree.***

**Prerequisites:** You must be an Owner or Developer(engineer) to use this method. 

**You must provide at least ONE of the following params: dataset, dataset_name, dataset_id.**

**param dtlpy.entities.dataset.Dataset dataset**
- Dataset Object

**param str dataset_name**
- The Name of the Dataset

**param str dataset_id**
- The Id of the Dataset

**return**
- DirectoryTree

**Example:**
```python
directory_tree = dl.datasets.directory_tree(dataset='dataset_entity')
```
Let's run that example of the `Test_Dataset` we created:
```python
directory_tree = proj.datasets.directory_tree(dataset_name='Test_Dataset')
directory_tree.tree

```
The output of the `directory_tree.tree` should look similar to this:
```python
{'value': {'id': '645e54554da725a6ed4553b9',
  'datasetId': '645e54554da72568414553b7',
  'url': 'https://gate.dataloop.ai/api/v1/items/645e54554da725a6ed4553b9',
  'dataset': 'https://gate.dataloop.ai/api/v1/datasets/645e54554da72568414553b7',
  'createdAt': '2023-05-12T14:59:33.000Z',
  'dir': '/',
  'filename': '/',
  'type': 'dir',
  'hidden': False,
  'metadata': {},
  'name': '',
  'creator': 'email@gmail.com',
  'items': 'https://gate.dataloop.ai/api/v1/datasets/645e54554da72568414553b7/items/645e54554da725a6ed4553b9/items',
  'export': {'zip': 'https://gate.dataloop.ai/api/v1/datasets/645e54554da72568414553b7/annotations/zip?directory=/',
   'json': 'https://gate.dataloop.ai/api/v1/datasets/645e54554da72568414553b7/annotations/json?directory=/'}},
 'children': []}
```
---------------------------
## <a name="download_annotations"></a> dl.datasets.download_annotations()
The `dl.datasets.download_annotations()` method allows you to download the Annotations and Items from a Dataset, depending on the Filter you are using. You can download as a mask, instance or an image mask of the Item.

You can see all of the details about this method below.

### download_annotations()

Definition: ` download_annotations(dataset: entities.Dataset, local_path: str=None, filters: entities.Filters=None, annotation_options: entities.ViewAnnotationOptions=None, annotation_filters: entities.Filters=None, overwrite: bool=False, thickness: int=1, with_text: bool=False, remote_path: str=None, include_annotations_in_output: bool=True, export_png_files: bool=False, filter_output_annotations: bool=False, alpha: float=None, export_version=entities.ExportVersion.V1) -> str`

***Download a Dataset's Annotations and/or Items by filters. You may filter the Dataset both for Items and for Annotations, and download them. Optionally you can download Annotations as: mask, instance, image mask of the Item.***


**Prerequisites:** You must be in the role of Owner or Developer(engineer).

**param dtlpy.entities.dataset.Dataset dataset**
- Dataset object

**param str local_path**
- Local folder save location (and/or saved filename)  

**param dtlpy.entities.filters.Filters filters**
- Filters entity or a dictionary containing filters parameters

**param list annotation_options**
- Type of download annotations: list(dl.ViewAnnotationOptions)

**param dtlpy.entities.filters.Filters annotation_filters**
- Filters entity to filter annotations for download

**param bool overwrite**
- (optional) By default = False so it doesn't overwrite the existing files

**param int thickness**
- (optional) - line thickness, if -1 annotation will be filled, default =1

**param bool with_text**
optional - add text to annotations, default = False

**param str remote_path**
DEPRECATED and ignored

**param bool include_annotations_in_output**
default - False , if export should contain annotations

**param bool export_png_files**
default - if True, semantic annotations should be exported as png files

**param bool filter_output_annotations**
default - False, given an export by filter - determine if to filter out annotations

**param float alpha**
opacity value [0 1], default 1

**param str export_version**
exported items will have original extension in filename, V1 - no original extension in filenames

**return**
local_path of the directory where all the downloaded Item were placed

**rtype**
str

Example:
```python
            #dl. or proj. (the project object/variable's name)
file_path = dl.datasets.download_annotations(dataset='dataset_entity',
                                     local_path='C:\\Users\\User\\Desktop\\dataloop_code_docs',
                                     #(optional)annotation_options=dl.ViewAnnotationOptions,
                                     overwrite=False,
                                     thickness=1,
                                     with_text=False,
                                     alpha=1
                                     )
```
In our case, a working example would be:
```python
# the dataset is d_set, or the variable in which you got the dataset object
#Optionally, you can do
#d_set = dl.datasets.get(dataset_name='Test_Dataset') #or your dataset's name/id
file_path = dl.datasets.download_annotations(dataset=d_set,
                                     local_path='local_path',
                                     #(optional)annotation_options=dl.ViewAnnotationOptions,
                                     overwrite=False,
                                     thickness=1,
                                     with_text=False,
                                     alpha=1
                                     )
```
And you'll get as an output a command progress bar and a download progress bar (wait for them to finish):
```python
Command Progress: 100%|██████████████████████████████████████████████████████████████| 100/100 [00:01<00:00, 53.51it/s]
Download Items: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 10.14it/s]
```
You can then print the `file_path` to see where your files were placed:
```python
print(file_path)
```
Which will show you where the files were saved:
```python
C:\Users\User\Desktop\dataloop_code_docs
```
**Note:** If you have no Items and no Annotations, a folder will be created where you will find an empty folder named `json`.
