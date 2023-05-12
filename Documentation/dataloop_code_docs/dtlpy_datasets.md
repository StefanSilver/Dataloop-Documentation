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
