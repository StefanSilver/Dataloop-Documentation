# Projects (dtlpy.projects)

In this section we will describe all of the methods (or functions) that can be applied to the Project Object in Dataloop.


## dl.projects.get()

The `dl.projects.get()` or `.get()` method in for the `projects` objects, is used to `GET` a Dataloop Project from the platform, in the current code you are working on.

The complete description for this method can be seen below:

### get

**Definition:**  ```python get(project_name: str=None, project_id: str=None, checkout: bool=False, fetch: bool=None, log_error=True) -> entities.Project ```

Gets a Project object from Dataloop.

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

```python project = dl.projects.get(project_id='project_id')```

You can see an example about how to use this, to get a project by name, below.
