# Projects (dtlpy.projects)

In this section we will describe all of the methods (or functions) that can be applied to the Project Object in Dataloop.

Below, you can see a Hyperlink list of all the methods for the .project object, which you can click to jump to the function/method you want to explore.

[dl.projects.get()](#get) | [dl.projects.create()](#create) | [dl.projects.list() ](#list) | [dl.projects.list_members()](#list_members) | [dl.projects.add_member()](#add_member) | [dl.projects.checkout()](#checkout) | [dl.projects.open_in_web()](#open_in_web) | [dl.projects.remove_member()](#remove_member)



-------------------------------------------
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

-------------------------------------------
## <a name="get"></a> dl.projects.get() 

The `dl.projects.get()` or `.get()` method in for the `projects` objects, is used to `GET` a Dataloop Project from the platform, in the current code you are working on.

The complete description for this method can be seen below:

### get()

**Definition:**  ` get(project_name: str=None, project_id: str=None, checkout: bool=False, fetch: bool=None, log_error=True) -> entities.Project `

**Gets a Project object from Dataloop.**

**Prerequisites:** You must be in the role of an Owner to get a Project object.

You must check out to a project or provide at least one of the following params: `project_id`, `project_name`

**param str project_name**
- (optional) search by name

**param str project_id**
- (optional) search by id

**param bool checkout**
- set the project as a default project object (cookies)

**param bool fetch**
- (optional)fetch entity from platform (True), default taken from cookie

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
-------------------------------------------
## <a name="create"></a> dl.projects.create() 
The `dl.projects.create()` allows you to create a new Project in the Dataloop Platform, in your current Organization.

You can see the complete description of the `.create()` method, along with its parameters and examples, below:

### create()
**Definition:** ` create(project_name: str, checkout: bool=False) -> entities.Project `

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

-------------------------------------------
## <a name="list"></a> dl.projects.list() 
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
-------------------------------------------
## <a name="list_members"></a> dl.projects.list_members()
The `dl.projects.list_members` method is used to show all of the members that have access to a give Project. 

You can see all of the details about this method, below:
### list_members()
**Definition:**` list_members(project: entities.Project, role: entities.MemberRole=None)`

Get a list of the members inside of a Project.

**Prerequisites:** You must be in the role of an Owner to list Project members.

**param dtlpy.entities.project.Project project**
- Project object

**param role**
- The required role for the user. The Roles can be ANNOTATION_MANAGER, ANNOTATOR, OWNER, DEVELOPER.

**return**
- list of the Project members

**rtype**
- list

**Example:**
```python 
project = dl.projects.get(project_name='CreatureHunt') # you need to first get 
dl.projects.list_members(project) # project variable was declared above, where we used `get()` to get a project in a variable
```
The output from the Example code above, should be something similar to this:
```python
[User(created_at=1668006935461, name='bill', last_name=None, username='email@dataloop.ai', email='email@dataloop.ai', role='owner', type=None, org='18739a63-4393-43ea-a87e-9a284b14978f', id='email@dataloop.ai'),
 User(created_at=1682936549405, name='model-mgmt-bot-1682936548922@dataloop.ai', last_name='Botman', username='bot.89b1cf81-6090-40a4-b2ad-48f7859ce5c4', email='bot.89b1cf81-6090-40a4-b2ad-48f7859ce5c4@bot.dataloop.ai', role='engineer', type='bot', org='18739a63-4393-43ea-a87e-9a284b14978f', id='bot.89b1cf81-6090-40a4-b2ad-48f7859ce5c4@bot.dataloop.ai'),
 User(created_at=1591079098237, name='Irina ', last_name='Afanasyeva', username='email@dataloop.ai', email='email@dataloop.ai', role='owner', type=None, org='38ba8434-747a-49d4-b121-d73eec74e2f8', id='email@dataloop.ai'),
 User(created_at=1673461599365, name='myfuncont', last_name=None, username='email@gmail.com', email='email@gmail.com', role='owner', type=None, org='18739a63-4393-43ea-a87e-9a284b14978f', id='email@gmail.com')]
```
You can also look for users with specific roles, which can be `.ANNOTATION_MANAGER`, `.ANNOTATOR`, `.OWNER`, `.DEVELOPER`. Use the code below, changing what type of user you are looking for:
```python
project = dl.projects.get(project_name='CreatureHunt') # you need to first get
dl.projects.list_members(project, role=dl.MemberRole.OWNER) 
```
The code above will list all users with OWNER role in the Project you selected.
-------------------------------------------
## <a name="add_member"></a> dl.projects.add_member()
The `dl.projects.add_member()` method is used to add additional members to the Project you are currently working on, and designating those new members' role.

Below, you can see all of the details of the `add_member()` method, and an example of its use.

### add_member()
**Definition:** `add_member(email: str, project_id: str, role: entities.MemberRole=entities.MemberRole.DEVELOPER)`

Add a member to the project.

**Prerequisites:** You must be in the role of an owner to add a member to a project.

**param str email**
- member email

**param str project_id**
- The Id of the project

**param role**
- The required role for the user. Use the enum dl.MemberRole

**return**
- dict that represent the user

**rtype**
- dict

**Example:**
```python
dl.projects.add_member(project_id='project_id', email='user@dataloop.ai', role=dl.MemberRole.DEVELOPER)
```
You can see a real example of this method's use in the code below:
```python
# Change the Project ID to your Project's ID, and the Email with the email of the user you want to add the Project
dl.projects.add_member(project_id='4c74c1b5-e9cb-4294-b9d5-cbfa13eda242', email='email@gmail.com', role=dl.MemberRole.DEVELOPER)
```
**Note:** The roles available are OWNER, DEVELOPER, ANNOTATOR, and ANNOTATION_MANAGER.
After executing this code, you will get a list of details about all users that are inside of that Project, including the one you just added, similar to what you can see below:
```python
[{'role': 'engineer',
  'membershipType': 'member',
  'membershipEntityId': '4c74c1b5-e9cb-4294-b9d5-cbfa13eda242',
  'denyMembersManagement': None,
  'guest': None,
  'domain': 'gmail.com',
  'createdAt': 1682933875445,
  'updatedAt': 1682946019262,
  'id': 'email@gmail.com',
  'username': 'email@gmail.com',
  'firstName': 'email',
  'lastName': None,
  'email': 'email@gmail.com',
  'avatar': 'https://lh3.googleusercontent.com/a/AGNmyxZ0mChamopWqD60G9WfnQNctHJoSdGSleVP7j6H=s96-c',
  'type': None,
  'lastLogin': 1682946019262,
  'lastLogout': None,
  'interest': None,
  'boarded': False,
  'hash': 'dba6984594271e36dab60954f15e5e140bfec294dbfb9cd3f08695f12f758cee',
  'timezone': None,
  'cookieApproval': None,
  'org': None}]
```

-------------------------------------------
## <a name="checkout"></a> dl.projects.checkout()
The `dl.projects.checkout()` method lets you change the current Project you are working on with another one.

You can see this method and its detailed description below:

### checkout()
**Definition:** ` checkout(identifier: str=None, project_name: str=None, project_id: str=None, project: entities.Project=None)`

***Checkout (or switch) to a project to work on.***

**Prerequisites:** All users can checkout.

You must provide at least ONE of the following params: `project_id`, `project_name`.

**param str identifier**
- Project name or partial id that you wish to switch

**param str project_name**
- The Name of the Project

**param str project_id**
- The Id of the project

**param dtlpy.entities.project.Project project**
- project object

**Example:**
```python
dl.projects.checkout(project_id='project_id')
```
You can see a working example below:
```python
# You can find all of your Projects and their IDs using dl.projects.list()
dl.projects.checkout(project_id='4c74c1b5-e9cb-4294-b9d5-cbfa13eda242')
```
Or you can use the Project's name instead of the ID:
```python
# You can find all of your Projects and their IDs using dl.projects.list()
dl.projects.checkout(project_name'CreatureHunt')
```
This command doesn't have any visible Output, but your Project will be switched to the Project you added to `project_id` or `project_name`.

-------------------------------------------
## <a name="open_in_web"></a> dl.projects.open_in_web()
The `dl.projects.open_in_web()` method allows you to open the Project you are currently working on (or a Project that you can select by ID) in the WebUI version of Dataloop.

You can see the full details of this methods, and use examples below.

### open_in_web()
**Definition:** `open_in_web(project_name: str=None, project_id: str=None, project: entities.Project=None)`

***Open the project in our web platform.***

Prerequisites: All users can open a Project in the WebUI of Dataloop.

**param str project_name**
- The Name of the Project

**param str project_id**
- The Id of the Project

**param dtlpy.entities.project.Project project**
- Project object

**Example:**
```python
dl.projects.open_in_web(project_id='project_id') # or project_name='project_name'
```
Select the `project_id` or the `project_name` in the command above, if you want to open a specific Project. If you use it without any parameters, the method will open the Project you currently have selected in the WebUI:
```python
dl.projects.open_in_web()
```
This will open a new browser page showing the details of your Project in Dataloop's WebUI:
![image](https://github.com/StefanSilver/Dataloop-Documentation/assets/58508793/a48a4566-7615-4ee5-b533-afd37be25c39)


-------------------------------------------
## <a name="remove_member"></a> dl.projects.remove_member()
The `dl.projects.remove_member()` method allows you to remove a member from an existing Project which you own.

You can find the details of this method, below.
### remove_member()
**Definition:** `remove_member(email: str, project_id: str)`

***Remove a member from a Project. Must be Owner. Cannot Remove Owners***

Prerequisites: You must be in the role of an Owner to delete a member from a Project.

**param str email**
- member email

**param str project_id**
- the Id of the Project

**return**
- dict that represents the user

**rtype**
- dict

**Example:**
```python
dl.projects.remove_member(project_id='project_id', email='user@dataloop.ai')
```
After runing the example above (after changing the `project_id` with your Project's ID and the `email` variable with the email of the email of the user you want to remove, you will get a list of all of the remaining users of that Project, without the user you just removed, which means that you successfully removed a memeber from the Project.

-------------------------------------------
## <a name="update"></a> dl.projects.update()
The `dl.projects.update()` method allows you to update the details of a Project, after you changed something it it.

You can find the details of this method, below.

### update()
**Definition:** `update(project: entities.Project, system_metadata: bool=False) -> entities.Project`

***Updates a Project's information (e.g., name, member roles, etc.).***

**Prerequisites:** Anyone can Update a Projects.

**param dtlpy.entities.project.Project project**
- project object

**param bool system_metadata**
- optional - True, if you want to change metadata system

**return**
- Project object

**rtype**
- dtlpy.entities.project.Project

**Example:**
```python
project = dl.projects.update(project='project_entity')
```
You can see an example of this code below:
```python 
dl.projects.update(project = 'CreatureHunt')
```
-------------------------------------------
## <a name="update_member"></a> dl.projects.update_member()
The `dl.projects.update_member()` method allows you to update the details of a memeber, including changing its role. However you need to be the Owner of the Project, to do this.

You can see the full details about this method, and an example of its use, below.
### update_member()
**Definition:** `update_member(email: str, project_id: str, role: entities.MemberRole=entities.MemberRole.DEVELOPER)`

***Updates a member's information/details in a specific Project.***

Prerequisites: You must be in the role of an Owner to update a member.

**param str email**
- member email

**param str project_id**
- The Id of the project

**param role**
- The required role for the user. Use the enum dl.MemberRole

**return**
- dict that represent the user

**rtype**
- dict

**Example:**
```python
dl.projects.update_member(project_id='project_id', email='user@dataloop.ai', role=dl.MemberRole.DEVELOPER)
```
A working example will look like this:
```python
dl.projects.update_member(project_id='4c74c1b5-e9cb-4294-b9d5-cbfa13eda242',email='email@gmail.com',role=dl.MemberRole.DEVELOPER)
```
The output of this code will  be a dict list of all members that are part of the Project, and their roles. For example, using that code, we changed the role of `email@gmail.com` from the ANNOTATOR role, which he had previously, to the DEVELOPER role (engineer in the printed details below), which he has now, after our change.
```python
[{'createdAt': 1683646354858,
  'id': 'email@gmail.com',
  'username': 'email@gmail.com',
  'firstName': 'email@gmail.com',
  'email': 'email@gmail.com',
  'domain': 'gmail.com',
  'lastName': '',
  'avatar': 'https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png',
  'role': 'engineer',
  'lastLogin': None,
  'guest': None,
  'membershipType': 'member',
  'membershipEntityId': '4c74c1b5-e9cb-4294-b9d5-cbfa13eda242',
  'denyMembersManagement': None}]
```

## Final Words
