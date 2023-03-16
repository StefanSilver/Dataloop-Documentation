# Annotations Validation

Annotation validation enables project managers to enforce almost any kind of Annotation rules. By loading a JavaScript file in the Annotation studio and running it when Annotators click on the Action button to assign an Item with a status, developers can build and enforce any kind of restrictions, such as:

- Labels that cannot co-exist (for example you cannot label both genders in an image with 1 person);
- Number of polygon points;
- Area or segmentation masks (avoid large masks);
- Minimum number of Labels required.

## Using Annotation Validation

### Part 1: Adding the script file to the Dataset's Recipe
To use the Annotation Validation capability of the Dataloop platforn, you need to go through a series of steps. Firstly, you need to [sign in and then log it into the veb-view of the platform](https://dataloop-production.auth0.com/login?state=hKFo2SBPMlg1clc2RkNWa1pfUEFvaXotSXI5OFd6NDNiQ1lBeaFupWxvZ2luo3RpZNkgSGVsWUVZUnFYZzVUREcxN09WdWdHeHlWam5NWFA1MW6jY2lk2SBGckcwSFpnYTFDSzVVVlVTSkp1RGtTRHFJdFBpZVdHVw&client=FrG0HZga1CK5UVUSJJuDkSDqItPieWGW&protocol=oauth2&response_type=id_token%20code&response_mode=form_post&redirect_uri=https%3A%2F%2Fgate.dataloop.ai%2Fadmit%3Fdefault&scope=openid%20email%20profile%20offline_access&nonce=_iAYyYyIqeAHngzZdkAsfdOUq0H5i6Nk&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMS4zIn0%3D).

Once you log in, you should see your Dashboard, and all of your Projects (if you have any). You must then select the Project you want to work on, and to which you want to apply Annotation Validation. In this example, we will use the CreatureHunt Project which has the Creatures Dataset, and is used for an [advanced onboarding exercise](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/11_onboarding_exercise.md) we created for Developers who use our Python SDK. Once you selected your project, you should see something similar to this:
https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/11_onboarding_exercise.md

You must then go on the left-side of your screen, so that the pannel opens up, and click on ```Data Management```:

![image](https://user-images.githubusercontent.com/58508793/225668417-a57c0cee-e461-4170-9fc2-9082cf54b15b.png)

Then, you should click on ```Recipes```, which will open up the page where you can see all of the Recipes available in the Project. If it's a new Project, you should only have a single Recipe:

![image](https://user-images.githubusercontent.com/58508793/225669134-59ac56b7-5d6e-4878-b9b0-fd0444c3d4fc.png)

Now, click on the ```Open Recipe``` button on the right-side of the page:

![image](https://user-images.githubusercontent.com/58508793/225670675-29f76506-1cfb-4c96-9462-26e8bb0aa60c.png)

After you click it, a new page should open up, where you can see the Default Recipe:

![image](https://user-images.githubusercontent.com/58508793/225671309-2a404169-35d1-4196-80ce-a2ae1b3ddd78.png)

You need to now click on the ```Instructions``` tab, which should look like this:

![image](https://user-images.githubusercontent.com/58508793/225671704-f40db559-95ce-4bd3-866c-8c26aed046d3.png)

You now need to locate the "Annotation Verification" section and click on the upload button to select and upload your JS validation script file: 

![image](https://user-images.githubusercontent.com/58508793/225672898-70977ad7-0ab2-4ec7-b5f5-2b3d7d18ae50.png)

After clicking it, you will need to search for a .js file containing the Validation Script. 

If you don't have one, add the code below to a .js file - you can also just create a new `.txt` file, place this in that `.txt` file, and then change the extension of the file from `.txt` to `.js`. Here's the code to force only a single Annotation for each Item, in your dataset:
```javascript
function validateAnnotations(annotationsArr) {
    //get all annotations in image
    let result = {}
    result.ok = true //or false
    result.errorMessage = "some message to display to user"
    result.errors = []
	console.log(annotationsArr.length)
    if (annotationsArr.length != 1){
        result.errorMessage = `there are ${annotationsArr.length} annotations. should only be one.`
        result.ok = false
    }

    return result
}
```
Once you successfully select the file and upload it, you should see a prompt notifying you that the file was successfully uploaded. You should also be able to see the file directly under the Annotations Verification, as you can see below:

![image](https://user-images.githubusercontent.com/58508793/225678251-57f9e5f4-a30f-44e3-85bb-a2a970631dbe.png)


The file can be removed to allow changing versions; however, only a single script file can work in any Recipe at a given time. To remove a file, you simply need to click the `X` button you can observe to the right-side of the `.js` file you just uploaded:
![image](https://user-images.githubusercontent.com/58508793/225679304-5720a8ef-f894-4e2b-9751-d3ad6cc870b2.png)

**Note:** Remember to SAVE CHANGES before exiting the page!
### Part 2: Running the Annotation Verification Script
To test the Annotation Verification script we just added, we must create a new Annotation Task that has the same Recipe as the one we added the script file to. If you want to learn how to do that, visit the documentation that teaches you how to "[Create an annotation task](https://dataloop.ai/docs/create-task)".

The short version to create a new Task, is to go to the left-side pannel on Dataloop's platform, click on `Workflows` and then click on `Tasks`. You should see a page similar to this one:

![image](https://user-images.githubusercontent.com/58508793/225700194-f9389c79-e27d-428a-a05b-e31a9ab64412.png)

You can now click to create a new Task. Then you can just press `Next` to the first page, after selectin a name for the Task. On the second step, you will need to select the Dataset you are working on - select the same one you used earlier. 

![image](https://user-images.githubusercontent.com/58508793/225701840-e1c9e23d-25b0-4230-8601-c9575ee72fcd.png)

On the `Instructions` page, which comes next, you need to select the Recipe on which you uploaded the `.js` script:

![image](https://user-images.githubusercontent.com/58508793/225702328-7db4e828-3ad5-4972-8a3e-a687c9e36c0d.png)

After that, just select the Contributors, and press next until you finish the Task creation. This may take a bit, but you should have a new task.

Now, you need to enter the Annotation Studio. When entering the Annotation studio from the task/assignment page, the `.js` file we added  is loaded automatically in the background, ready to be run. 

If you don't know how to get to the Annotation Studio, you must first go to `Workflows` -> `Tasks`, where you should see your Project's Tasks. Something similar to this:

![image](https://user-images.githubusercontent.com/58508793/225705965-b82f0e8d-5806-477c-8ada-5d7de740fcf2.png)

You must then double-click the Task you added the script file to, in our case it's "CreatureHunt-4". After double clicking it, an Assignments page will open up:

![image](https://user-images.githubusercontent.com/58508793/225708096-fe1f4698-6ad7-497a-a10a-46be8ce05dd5.png)

Now double-click that Assignment, and it should open up the Annotation Studio:
![image](https://user-images.githubusercontent.com/58508793/225708703-5f78297b-f221-4d42-95b3-ba9efb4e5d22.png)


Again, when entering the Annotation studio from the task/assignment, the `js` file we added will be loaded in the background, ready to be run. To see the script of that file, press the button on the right-side of the `Complete` button, highligted in the image below:

![image](https://user-images.githubusercontent.com/58508793/225709295-df7a00d8-2386-47f1-a911-d339fbb13e8e.png)

After clicking it, the script we added earlier should open up (you can also edit the script here):

![image](https://user-images.githubusercontent.com/58508793/225709632-61872781-82d7-4bde-bf8e-05595e81a33f.png)


If you now create Annotations and press the actions button to set COMPLETED or any other status - the JS file will be executed automatically. 

For example, since the script forces each Item in the Dataset to have exactly 1 Annotation, you can try simply pressing the `Complete` button, without adding any Annotation. if you do this, you will see that the platform won't let you, because of the script you just added:

![image](https://user-images.githubusercontent.com/58508793/225711248-0773ab38-ffb3-4f94-a8c2-b34460c9adeb.png)



![image](https://user-images.githubusercontent.com/58508793/225603459-715c79c1-8f58-4a03-ae5f-79f5cc6fcab9.png)
-------
![image](https://user-images.githubusercontent.com/58508793/225603388-36579bf1-9373-4a18-8bce-d7697b1e1b85.png)

7. Once the validation script finish running, a toast message will pop up with a success/error message, as defined in the functions returned object;

![image](https://user-images.githubusercontent.com/58508793/225603663-6e4da15b-7c1e-4f09-b453-05b23f89637f.png)

8. In case of an error, specific annotations that failed to comply with the validation scripts' rules will be flagged as problematic. An annotation-specific error message will be displayed in a tooltip on mouse hover.
![image](https://user-images.githubusercontent.com/58508793/225603802-e3ba3122-867c-4042-aa1f-96e8ee600659.png)


### Script Guielines

Your JS validation script should follow these guidelines:
1. Validation must occur in a function named ```validateAnnotations```;
2. The function should get Annotations object as an argument, which is an array of Annotation objects;
3. The function must return an object with the following interface:
```
{
    ok: boolean
    errorMessage?: string
    errors?: { [annotationId: string]: string }
}

```


### Debugging
To debug the validation script while in the annotation-studio, use Javascript debugging - ```console.log/debugger``` and inspect in your DevTools.

To see coordinates of annotations in the studio, which can help analyze the scripts work/behavior, use the _def property.
![image](https://user-images.githubusercontent.com/58508793/225604778-900bce2b-614b-4431-858e-af6469fe008b.png)

### Annotation Object

When interpertrating and referring to annotations received in the Annotations object, their properties comply with Dataloops' standard annotation JSON format, as [documented here in full](https://dataloop.ai/docs/annotation-json-format).


### Sample Validation Scripts

Sample 1 - Only a single annotation can be on the item.
```
 function validateAnnotations(annotationsArr) {
    //get all annotations in image
    let result = {}
    result.ok = true //or false
    result.errorMessage = "some message to display to user"
    result.errors = []
	console.log(annotationsArr.length)
    if (annotationsArr.length != 1){
        result.errorMessage = `there are ${annotationsArr.length} annotations. should only be one.`
        result.ok = false
    }

    return result
}
```

Sample 2 - A Polygon must have 6 points
```
function validateAnnotations(annotations) {
    const result = {
        ok: true,
        errors: {}
    }
    for (const a of annotations) {
        if (a.type === `segment` && a._def[0].length !== 6) {
            result.ok = false
            result.errors[a.clientId] = `Polygon must have 6 points`
        }
    }
    if (!result.ok) {
        result.errorMessage = `Some annotations have to be fixed`
    }
    return result
}
```

Sample 3 - Box annotations must have a parent annotation
```
function validateAnnotations(annotations) {
    const result = {
        ok: true,
        errors: {}
    }
    for (const a of annotations) {
        if (a.type === 'box') {
            if (!a.metadata.system.parentId) {
                result.ok = false
                result.errors[a.clientId] = 'Box annotation must have a parent'
            }
            }
        }
        if (!result.ok) {
              result.errorMessage = `Some annotations have to be fixed`
        }
        return result
}
```
