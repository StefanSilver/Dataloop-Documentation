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

