# Projects (dtlpy.projects)

In this section we will describe all of the methods (or functions) that can be applied to the Project Object in Dataloop.

Below, you can see a Hyperlink list of all the methods for the .project object, which you can click to jumpt to the function/method you want to explore.

[dl.projects.get()](#get) | [dl.projects.create()](#create) | [dl.projects.list() ](#list)

## Import dtlpy and Log In to Dataloop
The first thing you must do whenever you use Dataloop's Python SDK package `dtlpy` is to import the package and log in to Dataloop. If you don't have an account, [please register one here](https://console.dataloop.ai/welcome) or [read our Log In Onboarding](https://developers.dataloop.ai/onboarding/02_login_and_project_and_dataset_creation/). Also, if you don't have the `dtlpy` package installed, [read our Installation Onboarding](https://developers.dataloop.ai/onboarding/01_python_sdk_installation/).

In the code below, we import `dtlpy` as `dl` for easier use, and log in to Dataloop.
```python
import dtlpy as dl

# Logging in to Dataloop (checks if token expired ~24h expiration time for token - otherwise it doesn't run) - runs only once
if dl.token_expired():
   dl.login()
# you can also use the simple login() below - but you will have to log in every time you execute the code (not recommended)
#dl.login()
```


## <a name="get"></a> dl.projects.get() 

The `dl.projects.get()` or `.get()` method in for the `projects` objects, is used to `GET` a Dataloop Project from the platform, in the current code you are working on.

The complete description for this method can be seen below:

### get()

**Definition:**  ```python get(project_name: str=None, project_id: str=None, checkout: bool=False, fetch: bool=None, log_error=True) -> entities.Project ```

***Gets a Project object from Dataloop.***

**Prerequisites:** You must be in the role of an Owner to get a Project object.

You must check out to a project or provide at least one of the following params: `project_id`, `project_name`

**param str project_name**
    - optional - search by name

**param str project_id**
    - optional - search by id

**param bool checkout**
    - set the project as a default project object (cookies)

**param bool fetch**
    - optional - fetch entity from platform (True), default taken from cookie

**param bool log_error**
    - optional - show the logs errors

**return**
    - Project object

**rtype**
    - dtlpy.entities.project.Project

**Example:**

```python project = dl.projects.get(project_id='project_id') # change project_id with your Project's ID```

You can see an example about how to use this, to get a Project by name, below:
```python
dl.projects.get(project_name='CreatureHunt')
# or, if you want to get the Project in a variable use
project = dl.projects.get(project_name='CreatureHunt')
```
**Note:** If you use the second command, where you get the Project inside a variable, you need to use `project.print()` or `print(project)` to see the details from below.
If the code executes without errors, the output should look like this:
```python
Project(created_at=1676027918381, creator='email@gmail.com', id='4c74c1b5-e9cb-4294-b9d5-cbfa13eda242', name='CreatureHunt', feature_constraints=[{'name': 'downloadJsons', 'quota': 1, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 1, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 1, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 1, 'title': 'Create Driver'}])
```

## <a name="create"></a> dl.projects.create() 
The `dl.projects.create()` allows you to create a new Project in the Dataloop Platform, in your current Organization.

You can see the complete description of the `.create()` method, along with its parameters and examples, below:

### create()
**Definition:** ```python create(project_name: str, checkout: bool=False) -> entities.Project ```

***Creates a new Project.***

**Prerequisites:** Any User role can create a Project.

**param str project_name**
    - The Name of the Project

**param bool checkout**
    - set the project as a default project object (cookies)

**return**
    - Project object

**rtype**
    - dtlpy.entities.project.Project

**Example:**
```python project = dl.projects.create(project_name='project_name') ```

You can see an example about how to use this method, to create a new Project, below.
```python
# can only run once, when you first create the new Project.
dl.projects.create(project_name='Test_Project')
```
If the code executes right, you should get the following output:
```python
Project(created_at=1683624625465, creator='email@gmail.com', id='cfe67f7b-62cf-437b-8e05-8f60a4ef7c3a', name='Test_Project', feature_constraints=[{'name': 'downloadJsons', 'quota': 1, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 1, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 1, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 1, 'title': 'Create Driver'}])
```


## <a name="list"></a> dl.projects.list() 

## dl.projects.list()
The `dl.projects.list()` is used to show all of the Project objects in the current Organization. If you have only one Organization, that means it will return a list of all of your Projects.

You can see the complete description of the `.create()` method, along with its parameters and an example, below:

### list()

**Definition:** list() -> miscellaneous.List[entities.Project]

**Gets the user's project list**

**Prerequisites:** You must be a superuser to list all users' projects.

**return**
    - List of Project objects

Example:
```python 
dl.projects.list()
```

If you run the example code above, you will get an output that is similar to what you see below:
```python
[Project(created_at=1674492335504, creator='email@gmail.com', id='2ac5b20b-ec3b-4058-9d2f-cf6e41090b04', name='My-First-Project1', feature_constraints=[{'name': 'downloadJsons', 'quota': 0, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 0, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 0, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 0, 'title': 'Create Driver'}]),
 Project(created_at=1675184952443, creator='email@dataloop.ai', id='334469a6-a90c-4375-947b-a2810d7d08d8', name='Cool Project', feature_constraints=[{'name': 'downloadJsons', 'quota': 1, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 1, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 1, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 1, 'title': 'Create Driver'}]),
 Project(created_at=1676027918381, creator='email@gmail.com', id='4c74c1b5-e9cb-4294-b9d5-cbfa13eda242', name='CreatureHunt', feature_constraints=[{'name': 'downloadJsons', 'quota': 1, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 1, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 1, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 1, 'title': 'Create Driver'}])]
```
