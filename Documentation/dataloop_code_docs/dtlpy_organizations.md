# dtlpy.organizations

In Dataloop, an Organization refers to a management entity that provides a context for user accounts and facilitates collaboration, data sharing, and resource management. Here are some key points about Organizations in Dataloop:

- **Creation and Setup:** When setting up an account, an Organization is created and named, and it becomes linked to the account. If an account doesn't have an Organization, the user can contact Dataloop's support team for assistance. It's important to note that additional Organizations cannot be created; however, users can join existing Organizations by requesting the admin of the desired Organization to add them as a member.

- **Sub-Orgs and Client Orgs:** Dataloop allows customers or partners to have their own Organizations. This feature enables service providers to offer services and share projects with their clients. Customers/partners can sign up on the relevant platform, go through the onboarding process, and create their own Organization. As a result, they become annotation managers in the project and can access services, add workforce from their Organization, manage tasks, and more.

- **Active Organization:** As a member of one or more Organizations, users have an "Active organization" context. This means they can view the currently active Organization on the left-side menu. If a user belongs to multiple Organizations, they can switch the active Organization by clicking on the Organization name dropdown list and selecting the desired one.

- **Ownership of New Projects:** When creating new projects, they are automatically assigned to the currently active Organization. This ensures that the project's charges and ownership are attributed to the correct Organization. Before opening a new project, users should verify that the active Organization is set correctly.

- **Organization Overview:** The "Organization Overview" section provides a summary of all projects, datasets, tasks, and members within the current active Organization. It can be accessed from the left-side navigation menu.

- **Renaming Organization:** Admins and owners of an Organization have the ability to rename it. To do so, they can navigate to the Organization Overview, click on the Ellipsis icon menu item, and choose the "Rename Org" option.

- **Setting Paying-Account on Other Projects:** If a labeling service provider needs to account for work and resource consumption on a project owned by a different Organization (e.g., a client's project), they can set their organization's account as the paying subscription. This can be done by adding a user from the service provider organization as a 'Project owner' in the client's project. Then, on the service provider's dashboard, they can locate the project card, click the Ellipsis icon action button, and select "Set under [your organization name] account."

In this Documentation we will explore all of the methods available for the `dtlpy.organizations` in detail. If you want to look for a specific method, you can click one of the links below, which will take you to the method you are looking for.

------------------------

[dl.organizations.add_member()](#add_member) | [dl.organizations.delete_member()](#delete_member) | [dl.organizations.cache_action()](#cache_action)| [dl.organizations.get()](#get) | [dl.organizations.list()](#list) | [dl.organizations.list_groups()](#list_groups) | [dl.organizations.list_integrations()](#list_integrations) | [dl.organizations.list_members()](#list_members) | [dl.organizations.update()](#update) | 

------------------------

## Import dtlpy and log in to Dataloop

To use the `dtlpy` Python package and access Dataloop's platform, you must first import the package and log in to the platform.
```python
import dtlpy as dl
dl.setenv('prod')
#Logging in to Dataloop (checks if token expired ~24h expiration time for token)
if dl.token_expired():
   dl.login()
#you can also use the simple login: 
#dl.login()
```
-----------------------------------------------
## <a name="add_member"></a> dl.organizations.add_member()
The `dl.organizations.add_member()` method allows you add a new member in the Organization that you are currently working on.

You can see all of the details of this function, below.


### add_member()
**Definition:** `add_member(email: str, role: entities.MemberOrgRole=entities.MemberOrgRole.MEMBER, organization_id: str=None, organization_name: str=None, organization: entities.Organization=None)`

***Adds members to your Organization.***

**Prerequisities:** To add members to an organization, you must be an owner in that organization. You must provide at least ONE of the following params: `organization`, `organization_name`, or `organization_id`.

**param str email**
- the member's email

**param str role**
- MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER, MemberOrgRole.WORKER

**param str organization_id**
- Organization id

**param str organization_name**
- Organization name

**param entities.Organization organization**
- Organization object

**return**
- True if successful or error if unsuccessful

**rtype**
- bool

**Example:**
```python
dl.organizations.add_member(email='user@domain.com',
                            organization_id='organization_id',
                            role=dl.MemberOrgRole.MEMBER)
```
To find out your Organization's Id, run the code below, which will list all Organizations you have access to:
```python
dl.organizations.list()
```


The output should look similar to what you see below; and the `org` holds the ID of your Organization (in this case the id is `8c8387a3-e771-4d2b-ad77-6a30294dbd01`):
```python
Organization(members=[{'createdAt': 1673461599365, 'updatedAt': 1684341970595, 'id': 'email@gmail.com', 'username': 'email@gmail.com', 'firstName': 'email', 'lastName': None, 'email': 'myfuncont@gmail.com', 'avatar': 'https://lh3.googleusercontent.com/a/AEdFTp6uAS-yuhaaI-EU3BFR0fgHpd1_UJ7LS2_W3pXl=s96-c', 'type': None, 'lastLogin': 1684262059553, 'lastLogout': 1680528866969, 'interest': 'dataScience', 'boarded': True, 'hash': 'c32a01dfbaf29ac953bde5afba936af81dcea03cfabd61d5f28ad3f025f41435', 'timezone': None, 'cookieApproval': 1675420416926, 'org': '18739a63-4393-43ea-a87e-9a284b14978f'}], groups=[], account={'createdAt': 1674222447241, 'updatedAt': 1674222447241, 'id': '08e52acc-107c-4503-9997-0f8e99acaef1', 'name': "ssssssss's account", 'owner': 'email@gmail.com', 'org': '8c8387a3-e771-4d2b-ad77-6a30294dbd01', 'creator': 'myfuncont@gmail.com'}, created_at=1674222447224, updated_at=1674222447257)]
```
Once we have that , we can run the example code above, using this ID and the e-mail of the user we want to add to our Organization; remember you can set the role of the new user you are adding (MEMBER, OWNER, ADMIN, WORKER):
```python
dl.organizations.add_member(email='user@domain.com',
                            organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01',
                            role=dl.MemberOrgRole.MEMBER)
```
The output should be a simple `True` if you added the new user successfully, or `False` if the operation failed.
--------------------------
## <a name="delete_member"></a> dl.organizations.delete_member()
The `dl.organizations.delete_member()` method allows you delete a member in the Organization that you are currently working on.

You can see all of the details of this function, below.


### delete_member()
**Definition:** `delete_member(user_id: str, organization_id: str=None, organization_name: str=None, organization: entities.Organization=None, sure: bool=False, really: bool=False) -> bool`

***Deletes member from the Organization.***

**Prerequisites:** Must be an organization Owner to delete members. You must provide at least ONE of the following params: `organization_id`, `organization_name`, `organization`.

**param str user_id**
- user id

**param str organization_id**
- Organization id

**param str organization_name**
- Organization name

**param entities.Organization organization**
- Organization object

**param bool sure**
- Are you sure you want to delete?

**param bool really**
- Are you surely sure that you want to delete?

**return**
- True if success and error if not

**rtype**
- bool

**Example:**
```python
dl.organizations.delete_member(user_id='user_id',
                                organization_id='organization_id',
                                sure=True,
                                really=True)
```
To find out your Organization's Id, run the code below, which will list all Organizations you have access to:
```python
dl.organizations.list()
```
The output should look similar to what you see below; and the `org` holds the ID of your Organization (in the case of this Organization the id is `8c8387a3-e771-4d2b-ad77-6a30294dbd01` - yours will be different):
```python
Organization(members=[{'createdAt': 1673461599365, 'updatedAt': 1684341970595, 'id': 'email@gmail.com', 'username': 'email@gmail.com', 'firstName': 'email', 'lastName': None, 'email': 'myfuncont@gmail.com', 'avatar': 'https://lh3.googleusercontent.com/a/AEdFTp6uAS-yuhaaI-EU3BFR0fgHpd1_UJ7LS2_W3pXl=s96-c', 'type': None, 'lastLogin': 1684262059553, 'lastLogout': 1680528866969, 'interest': 'dataScience', 'boarded': True, 'hash': 'c32a01dfbaf29ac953bde5afba936af81dcea03cfabd61d5f28ad3f025f41435', 'timezone': None, 'cookieApproval': 1675420416926, 'org': '18739a63-4393-43ea-a87e-9a284b14978f'}], groups=[], account={'createdAt': 1674222447241, 'updatedAt': 1674222447241, 'id': '08e52acc-107c-4503-9997-0f8e99acaef1', 'name': "ssssssss's account", 'owner': 'email@gmail.com', 'org': '8c8387a3-e771-4d2b-ad77-6a30294dbd01', 'creator': 'email@gmail.com'}, created_at=1674222447224, updated_at=1674222447257)]
```
Once we have the Organization ID, we  also need the User's ID. To find the users in our Organization, and their IDs, we can run the code below:

```python
dl.organizations.list_members(organization_id='18739a63-4393-43ea-a87e-9a284b14978f')#your id will be different
```
Which will have an output similar to this; you need to take the `id` field, which we will use to delete the user:
```python
[User(created_at=1673461599365, name='email', last_name=None, username='email@gmail.com', email='email@gmail.com', role='owner', type=None, org='18739a63-4393-43ea-a87e-9a284b14978f', id='email@gmail.com'),
 User(created_at=1684342458768, name=None, last_name=None, username=None, email=None, role='member', type=None, org='8c8387a3-e771-4d2b-ad77-6a30294dbd01', id='6cdfccfb-ab06-4ed2-a585-b3a6674c1dc8')]
```
Remember you can set the role of the new user you are adding (MEMBER, OWNER, ADMIN, WORKER):
```python
dl.organizations.delete_member(user_id='6cdfccfb-ab06-4ed2-a585-b3a6674c1dc8',
                                organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01',
                                sure=True,
                                really=True)
```

The output should be a simple `True` if you added the new user successfully, or `False` if the operation failed.

------------------------------------------
## <a name="cache_action"></a> dl.organizations.cache_action()
The `dl.organizations.cache_action()` method allows you to add or remove Cache for an Organization that you own (are Admin/Owner) to.

You can see all of the details of this function, below.

### cache_action()

**Definition:** `cache_action(organization_id: str=None, organization_name: str=None, organization: entities.Organization=None, mode=entities.CacheAction.APPLY, pod_type=entities.PodType.SMALL)`

***Adds or remove Cache for an Organization you own.***

**Prerequisites:** You must be an organization owner. You must provide at least ONE of the following params: `organization`, `organization_name`, or `organization_id`.

**param str organization_id**
- Organization id

**param str organization_name**
- Organization name

**param entities.Organization organization**
- Organization object

**param str mode**
- dl.CacheAction.APPLY or dl.CacheAction.DESTROY

**param entities.PodType pod_type**
- dl.PodType.SMALL, dl.PodType.MEDIUM, dl.PodType.HIGH

**return**
- True if success

**rtype**
- bool

**Example:**
```python
dl.organizations.cache_action(organization_id='organization_id', #or organization_name='Dataloop' (your org name)
                              mode=dl.CacheAction.APPLY) #or .DESTROY
```
A working code would look like this, with your own Organization ID:
```python
dl.organizations.cache_action(organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01',
                              mode=dl.CacheAction.APPLY)
# You can also use
#dl.organizations.cache_action(organization_name='Dataloop',
#                              mode=dl.CacheAction.APPLY)
```
To find out your Organization's Id, run the code below, which will list all Organizations you have access to:
```python
dl.organizations.list()
```
------------
## <a name="get"></a> dl.organizations.get()
The `dl.organizations.get()` method allows you to `get` or activate an Organization, setting it as the active Organization in the current coding session.

You can see all of the details of this function, below.

### get()

**Definition:** `get(organization_id: Optional[str] = None, organization_name: Optional[str] = None, fetch: Optional[bool] = None)→ Organization[source]`

***Gets an Organization object to be able to use it in your code.***

**Prerequisites:** You must be a ***superuser*** to use this method. You must provide at least ONE of the following params: `organization_name` or `organization_id`.


**param organization_id (str)**
- (optional) search by id

**param organization_name (str)**
- (optional) search by name

**param fetch** 
- (optional) fetch entity from platform, by default taken from cookie

**Returns:**
- Organization object

**Return type:**
- dtlpy.entities.organization.Organization

**Example:**
```python
org = dl.organizations.get(organization_id='organization_id')
```
If you run the code below on your Organization's ID:
```python
dl.organizations.get(organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01') 
# You can also use
#dl.organizations.get(organization_name='Dataloo')
```

You should get an output similar to this:
```python
Organization(members=[{'createdAt': 1673461599365, 'updatedAt': 1684343644071, 'id': 'email@gmail.com', 'username': 'email@gmail.com', 'firstName': 'email', 'lastName': None, 'email': 'email@gmail.com', 'avatar': 'https://lh3.googleusercontent.com/a/AEdFTp6uAS-yuhaaI-EU3BFR0fgHpd1_UJ7LS2_W3pXl=s96-c', 'type': None, 'lastLogin': 1684262059553, 'lastLogout': 1680528866969, 'interest': 'dataScience', 'boarded': True, 'hash': 'c32a01dfbaf29ac953bde5afba936af81dcea03cfabd61d5f28ad3f025f41435', 'timezone': None, 'cookieApproval': 1675420416926, 'org': '18739a63-4393-43ea-a87e-9a284b14978f'}], groups=[], account={'createdAt': 1674222447241, 'updatedAt': 1674222447241, 'id': '08e52acc-107c-4503-9997-0f8e99acaef1', 'name': "ssssssss's account", 'owner': 'email@gmail.com', 'org': '8c8387a3-e771-4d2b-ad77-6a30294dbd01', 'creator': 'email@gmail.com'}, created_at=1674222447224, updated_at=1674222447257)
```

------------------------------------
## <a name="list"></a> dl.organizations.list()
The `dl.organizations.list()` method allows you to list all of the Organizations you have access to.

You can see all of the details of this function, below.

### list()

**Definition:** `list() -> miscellaneous.List[entities.Organization]`

***Lists all the organizations in Dataloop.***

**Prerequisites:** You must be a superuser to use this method.

**return**
- List of Organization objects

**rtype**
- list

**Example:**
```python
dl.organizations.list()
```
The output of this will be a list of all of the Organizations you have access to, and the users inside each organization:

```python
Organization(members=[{'createdAt': 1673461599365, 'updatedAt': 1684341970595, 'id': 'email@gmail.com', 'username': 'email@gmail.com', 'firstName': 'email', 'lastName': None, 'email': 'email@gmail.com', 'avatar': 'https://lh3.googleusercontent.com/a/AEdFTp6uAS-yuhaaI-EU3BFR0fgHpd1_UJ7LS2_W3pXl=s96-c', 'type': None, 'lastLogin': 1684262059553, 'lastLogout': 1680528866969, 'interest': 'dataScience', 'boarded': True, 'hash': 'c32a01dfbaf29ac953bde5afba936af81dcea03cfabd61d5f28ad3f025f41435', 'timezone': None, 'cookieApproval': 1675420416926, 'org': '18739a63-4393-43ea-a87e-9a284b14978f'}], groups=[], account={'createdAt': 1674222447241, 'updatedAt': 1674222447241, 'id': '08e52acc-107c-4503-9997-0f8e99acaef1', 'name': "ssssssss's account", 'owner': 'email@gmail.com', 'org': '8c8387a3-e771-4d2b-ad77-6a30294dbd01', 'creator': 'email@gmail.com'}, created_at=1674222447224, updated_at=1674222447257)]
```

---------------------------
## <a name="list_groups"></a> dl.organizations.list_groups()
The `dl.organizations.list_groups()` method allows you to list all of the Groups for an Organization you have access to.

You can see all of the details of this function, below.

### list_groups()

**Definition:** `list_groups(organization: entities.Organization=None, organization_id: str=None, organization_name: str=None)`

***Lists all organization groups (groups that were created within the organization).**

**Prerequisites:** You must be an organization owner to use this method. You must provide at least ONE of the following params: `organization`, `organization_name`, or `organization_id`.

**param entities.Organization organization**
- Organization object

**param str organization_id**
- Organization id

**param str organization_name**
- Organization name

**return**
- groups list

**rtype**
- list

**Example:**
```python
groups_list = dl.organizations.list_groups(organization_id='organization_id')
```
A working code would look like this, with your Organization's ID/Name:
```python
dl.organizations.list_groups(organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01')
#or
dl.organizations.list_groups(organization_name='Dataloop')

#or, if you want to use an Organization Object/Variable/Entity
org_entity=dl.organizations.get(organization_name='Dataloop')
dl.organizations.list_groups(organization = org_entity)
```

The output will look similar to this:
```python
[{'members': [{'createdAt': 1635162156689,
    'updatedAt': 1684335864862,
    'id': 'email@dataloop.ai',
    'username': 'email@dataloop.ai',
    'firstName': 'firstname',
    'lastName': 'lastname',
    'email': 'email@dataloop.ai',
    'avatar': 'https://lh3.googleusercontent.com/a/AATXAJwh57vW2eQpgdqtRraw5Eiic2wDIy4b7sWA9TdC=s96-c',
    'type': None,
    'lastLogin': 1684235662698,
    'lastLogout': None,
    'interest': 'dataManagement',
    'boarded': True,
    'hash': '3301f1d271445a55e54cce6d047eaedcc9a2a15ec78a11366e0fb31fbf2b3cff',
    'timezone': None,
    'cookieApproval': 1675261017431,
    'org': '38ba8434-747a-49d4-b121-d73eec74e2f8'}]
```
--------------------------------------
## <a name="list_integrations"></a> dl.organizations.list_integrations()
The `dl.organizations.list_integrations()` method allows you to list all of the Integrations you have with other external cloud storages.

You can see all of the details of this function, below.

### list_integrations()

**Definition:** `list_integrations(organization: entities.Organization=None, organization_id: str=None, organization_name: str=None, only_available=False)`

***Lists all Organization integrations with external cloud storages.***

**Prerequisites:** You must be an organization owner to use this method. You must provide at least ONE of the following params: `organization_id`, `organization_name`, or `organization`.

**param entities.Organization organization**
- Organization object

**param str organization_id**
- Organization id

**param str organization_name**
- Organization name

**param bool only_available**
- if True list only the available integrations

**return**
- integrations list

**rtype**
- list

**Example:**
```python
list_integrations = dl.organizations.list_integrations(organization='organization-entity',
                                    only_available=True)
```
A working code example can be seen below, in all the ways you can use this method:
```python
dl.organizations.list_integrations(organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01')
#or
dl.organizations.list_integrations(organization_name='Dataloop')

#or, if you want to use an Organization Object/Variable/Entity
org_entity=dl.organizations.get(organization_name='Dataloop')
dl.organizations.list_integrations(organization = org_entity)
```
The output should look similar to this:
```python
[{'metadata': [],
  'createdAt': 1632058672444,
  'updatedAt': 1632979485932,
  'id': '0141s9eb-es2b-495b-bs71-40a5a4f7ss2b',
  'name': 'Google Bucket images',
  'type': 'gcs',
  'org': '18739sa63-4393-4sea-a87e-9a2s4b14978f',
  'creator': 'email@dataloop.ai'},
 {'metadata': [],
  'createdAt': 1660119346351,
  'updatedAt': 1660119346351,
  'id': '029s5574-bcs6-4ds4-bac9-1fb6ass2ca8',
  'name': 'dadsa',
  'type': 'key_value',
  'org': '18739a63-43s3-43ea-a87e-9a2s4b14978f',
  'creator': 'email@dataloop.ai'}
```
--------------------------------
## <a name="list_members"></a> dl.organizations.list_members()
The `dl.organizations.list_members()` method allows you to list all of the Members that are part of your active Organization, and their specific details.

You can see all of the details of this function, below.

### list_members()

**Definition:** `list_members(organization: entities.Organization=None, organization_id: str=None, organization_name: str=None, role: entities.MemberOrgRole=None)`

***Lists all members inside of an Organization.***

**Prerequisites:** You must be an organization owner to use this method. You must provide at least ONE of the following params: `organization_id`, `organization_name`, or `organization`.

**param entities.Organization organization**
` Organization object

**param str organization_id**
- Organization's id

**param str organization_name**
- Organization's name

**param entities.MemberOrgRole role**
- MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER, MemberOrgRole.WORKER

**return**
- Projects list

**rtype**
- list

**Example:**
```python
list_members = dl.organizations.list_members(organization='organization-entity',
                            role=dl.MemberOrgRole.MEMBER)
```
Examples of working code of this method can be seen below:
```python
dl.organizations.list_members(organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01')
#or
dl.organizations.list_members(organization_name='Dataloop')

#or, if you want to use an Organization Object/Variable/Entity
org_entity=dl.organizations.get(organization_name='Dataloop')
dl.organizations.list_members(organization = org_entity)
```
The output should look like this:

```python
[User(created_at=1598174769386, name='name', last_name='lastname', username='email@dataloop.ai', email='email@dataloop.ai', role='admin', type=None, org='18739a63-4393-43ea-as7e-9a28s4b14978f', id='email@dataloop.ai'),
 User(created_at=1635162156689, name='name', last_name='lastname', username='email@dataloop.ai', email='email@dataloop.ai', role='owner', type=None, org='38ba8434-747a-49d4-b1s1-d73ees74e2f8', id='email@dataloop.ai')]
```
--------------------------
## <a name="update"></a> dl.organizations.update()
The `dl.organizations.update()` method allows you to update the Organization you select, if you are a Superuser in that Organization.

You can see all of the details of this function, below.

### update()

**Definition:** `update(plan: str, organization: entities.Organization=None, organization_id: str=None, organization_name: str=None) -> entities.Organization`

***Updates an Organization.***

**Prerequisites:** You must be a superuser to update an organization. You must provide at least ONE of the following params: `organization`, `organization_name`, or `organization_id` and the `plan` parameter.

**param str plan**
- OrganizationsPlans.FREEMIUM, OrganizationsPlans.PREMIUM

**param entities.Organization organization**
- Organization object

**param str organization_id**
- Organization id

**param str organization_name**
- Organization name

**return**
- organization object

**rtype**
- dtlpy.entities.organization.Organization

**Example:**
```python
dl.organizations.update(organization='organization-entity',
                        plan=dl.OrganizationsPlans.FREEMIUM)
```

An example of working code for updating an Organization can be seen below:
```python
dl.organizations.update(organization_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01',plan=dl.OrganizationsPlans.FREEMIUM)#.PREMIUM if you are a paying user
#or
dl.organizations.update(organization_name='Dataloop',plan=dl.OrganizationsPlans.FREEMIUM)#.PREMIUM if you are a paying user

#or, if you want to use an Organization Object/Variable/Entity
org_entity=dl.organizations.get(organization_name='Dataloop')
dl.organizations.update(organization = org_entity,plan=dl.OrganizationsPlans.FREEMIUM)#.PREMIUM if you are a paying user
```
If everything goes right, and you have the required access, you will get back an Organization Object, listing the current state of your Organization:
```python
Organization(members=[{'createdAt': 1673461599365, 'updatedAt': 1684341970595, 'id': 'email@gmail.com', 'username': 'email@gmail.com', 'firstName': 'email', 'lastName': None, 'email': 'email@gmail.com', 'avatar': 'https://lh3.googleusercontent.com/a/AEdFTp6uAS-yuhaaI-EU3BFR0fgHpd1_UJ7LS2_W3pXl=s96-c', 'type': None, 'lastLogin': 1684262059553, 'lastLogout': 1680528866969, 'interest': 'dataScience', 'boarded': True, 'hash': 'c32a01dfbaf29ac953bde5afba936af81dcea03cfabd61d5f28ad3f025f41435', 'timezone': None, 'cookieApproval': 1675420416926, 'org': '18739a63-4393-43ea-a87e-9a284b14978f'}], groups=[], account={'createdAt': 1674222447241, 'updatedAt': 1674222447241, 'id': '08e52acc-107c-4503-9997-0f8e99acaef1', 'name': "ssssssss's account", 'owner': 'email@gmail.com', 'org': '8c8387a3-e771-4d2b-ad77-6a30294dbd01', 'creator': 'email@gmail.com'}, created_at=1674222447224, updated_at=1674222447257)]
```

If you don't have the required permissions, you will get this error:
```python
Forbidden: ('403', ' You are not permitted to perform this  action. ')
```

-----------------------------------
