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
