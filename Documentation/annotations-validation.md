# Annotations Validation

Annotation validation enables Dataloop customers to enforce almost any kind of Annotation rules they can think of such as:

- Labels that cannot co-exist (for example you cannot label both genders in an image with 1 person)
- Number of polygon points
- Area or segmentation masks (avoid large masks)
- Minimum number of Labels required

You accomplish this by working with a user with a Developer role or above to load a JavaScript (JS) file in the Annotation studio.  The JS executes when Annotators click on the Action button to assign an Item with a status.

## Using Annotation Validation

### Before we get started - create a .js file to use in this exercise

If this is your first time working with this Annotation Validation technology, please create an empty `.js` file add the code below to to it.  

You can also just create a new `.txt` file, place this in that `.txt` file, and then change the extension of the file from `.txt` to `.js`. 

Here's the sample code that enforces a single Annotation for each Item in a Dataset:

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

### Part 1: Adding the script file to the Dataset's Recipe
To use the Annotation Validation capability of the Dataloop platforn, you need to go through a series of steps. First, you;ll need to [sign in to the Dataloop.ai Web UI](https://dataloop-production.auth0.com/login?state=hKFo2SBPMlg1clc2RkNWa1pfUEFvaXotSXI5OFd6NDNiQ1lBeaFupWxvZ2luo3RpZNkgSGVsWUVZUnFYZzVUREcxN09WdWdHeHlWam5NWFA1MW6jY2lk2SBGckcwSFpnYTFDSzVVVlVTSkp1RGtTRHFJdFBpZVdHVw&client=FrG0HZga1CK5UVUSJJuDkSDqItPieWGW&protocol=oauth2&response_type=id_token%20code&response_mode=form_post&redirect_uri=https%3A%2F%2Fgate.dataloop.ai%2Fadmit%3Fdefault&scope=openid%20email%20profile%20offline_access&nonce=_iAYyYyIqeAHngzZdkAsfdOUq0H5i6Nk&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMS4zIn0%3D).

Once you log in, click on the Dashboard icon if you don't already see it and you'll see a list of all of your Projects that you own or on which you are a assigned. You must then select the Project you want to work on, and to which you want to apply Annotation Validation. In this example, we will use the CreatureHunt Project which has the Creatures Dataset, and is used for the [advanced onboarding exercise](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/11_onboarding_exercise.md) we created for Developers who use our Python SDK. Once you selected your project, you should see something similar to this:


![image](https://user-images.githubusercontent.com/58508793/225881605-748f570d-b20a-43bb-87d5-04e503f4d09f.png)

You must then go to the left navigation panel on the left-side of your screen and click on ```Data Management```:

![image](https://user-images.githubusercontent.com/58508793/225668417-a57c0cee-e461-4170-9fc2-9082cf54b15b.png)

Then, click on ```Recipes```, which will open up the page where you can see all of the Recipes available in the Project. If it's a new Project, you might only have a single Recipe:

![image](https://user-images.githubusercontent.com/58508793/225669134-59ac56b7-5d6e-4878-b9b0-fd0444c3d4fc.png)

Now, click on the ```Open Recipe``` button on the right-side of the page:

![image](https://user-images.githubusercontent.com/58508793/225670675-29f76506-1cfb-4c96-9462-26e8bb0aa60c.png)

After you click it, a new page should open up, where you can see the Default Recipe or Recipe that is in use:

![image](https://user-images.githubusercontent.com/58508793/225671309-2a404169-35d1-4196-80ce-a2ae1b3ddd78.png)

You need to now click on the ```Instructions``` tab which should look like this:

![image](https://user-images.githubusercontent.com/58508793/225671704-f40db559-95ce-4bd3-866c-8c26aed046d3.png)

You now need to locate the "Annotation Verification" section and click on the `Upload` button to select and upload your JS validation script file: 

![image](https://user-images.githubusercontent.com/58508793/225672898-70977ad7-0ab2-4ec7-b5f5-2b3d7d18ae50.png)

After clicking it, you will need to search for the `.js` file that contains the Validation Script. 

Once you successfully select the file and upload it, you should see a prompt notifying you that the file was successfully uploaded. You should also be able to see the file directly under Annotations Verification, as you can see below:

![image](https://user-images.githubusercontent.com/58508793/225678251-57f9e5f4-a30f-44e3-85bb-a2a970631dbe.png)


Only a single script file can exist in a Recipe at any given time. To iterate versions of a `.js` file, you have to remove the current one then uploade the new version. To remove a file, you simply need to click the `X` button you can observe to the right-side of the `.js` file you just uploaded:

![image](https://user-images.githubusercontent.com/58508793/225679304-5720a8ef-f894-4e2b-9751-d3ad6cc870b2.png)

**Note:** Remember to SAVE CHANGES before exiting the page!
### Part 2: Running the Annotation Verification Script
To test the Annotation Verification script we just added, we must create a new Annotation Task that has uses the Recipe to which we just added the script file. If you want to learn how to create and Annotation Task, visit the documentation that teaches you how to "[Create an Annotation Task](https://dataloop.ai/docs/create-task)".

The short version to create a new Task, is to go to the left-side pannel on Dataloop's platform, click on `Workflows` and then click on `Tasks`. You should see a page similar to this one:

![image](https://user-images.githubusercontent.com/58508793/225700194-f9389c79-e27d-428a-a05b-e31a9ab64412.png)

You can now click to create a new Task. Then enter a name for the Task and press `Next`. On the second step, you will need to select the Dataset you are working on - select the same one you used earlier. 

![image](https://user-images.githubusercontent.com/58508793/225701840-e1c9e23d-25b0-4230-8601-c9575ee72fcd.png)

On the `Instructions` page, which comes next, you need to select the Recipe on which you uploaded the `.js` script:

![image](https://user-images.githubusercontent.com/58508793/225702328-7db4e828-3ad5-4972-8a3e-a687c9e36c0d.png)

After that, select the Contributors you want to assign the Task to and click next until you finish the Task creation. This may take a bit, but you should now have a new Task.

Now, you need to enter the Annotation Studio. When entering the Annotation studio from the Task/Assignment page, the `.js` file we added  is loaded automatically in the background, ready to be run. 

If you don't know how to get to the Annotation Studio, you must first go to `Workflows` -> `Tasks`, where you should see your Project's Tasks. Something similar to this:

![image](https://user-images.githubusercontent.com/58508793/225705965-b82f0e8d-5806-477c-8ada-5d7de740fcf2.png)

Assuming you assigned yourself as a Contributor, you should now have a Task assigned to you.  To get to this Task, you must then double-click the Task you added the script file to, in our case it's "CreatureHunt-4". After double clicking it, an Assignments page will open up:

![image](https://user-images.githubusercontent.com/58508793/225708096-fe1f4698-6ad7-497a-a10a-46be8ce05dd5.png)

Now double-click that Assignment, and it should open up the Annotation Studio:
![image](https://user-images.githubusercontent.com/58508793/225708703-5f78297b-f221-4d42-95b3-ba9efb4e5d22.png)


Again, when entering the Annotation Studio from the task/assignment, the `.js` file we added will be loaded in the background, ready to be run. To see the content of that file, press the button on the right-side of the `Complete` button, highligted in the image below:

![image](https://user-images.githubusercontent.com/58508793/225709295-df7a00d8-2386-47f1-a911-d339fbb13e8e.png)

After clicking it, the script we added earlier should open up (you can also edit the script here):

![image](https://user-images.githubusercontent.com/58508793/225709632-61872781-82d7-4bde-bf8e-05595e81a33f.png)


If you now create Annotations and press the actions button to set COMPLETED or any other status - the JS file will be executed automatically. 

For example, since the script we're using for this exercise forces each Item in the Dataset to have exactly 1 Annotation, you can try simply pressing the `Complete` button, without adding an Annotation. If you do this, you will see that the platform won't let you.  The script you just added is enforcing the need to have at least 1 Annotation.

![image](https://user-images.githubusercontent.com/58508793/225711248-0773ab38-ffb3-4f94-a8c2-b34460c9adeb.png)



**Important!**

Once the validation script we added finishes running, a message will pop up with a success/error message, as defined in the function's returned object:

![image](https://user-images.githubusercontent.com/58508793/225603663-6e4da15b-7c1e-4f09-b453-05b23f89637f.png)

After running the script, specific Annotations that failed to comply with the validation scripts' rules will be flagged as problematic. An Annotation-specific error message will be displayed in a tooltip on mouse hover.

![image](https://user-images.githubusercontent.com/58508793/225603802-e3ba3122-867c-4042-aa1f-96e8ee600659.png)

You can find the `Issues` section by going to `Workflows` -> `Issues`:

![image](https://user-images.githubusercontent.com/58508793/225888970-a5128d6e-de8d-4811-a20e-12e76a1a696c.png)




### Script Guielines
If you want to create other custom scripts, we higly recommend you follow the guidelines below so you won't encounter any problems.

Your JS validation script should follow these rules:

1. Validation must occur in a function named ```validateAnnotations```;
2. The function should get an Annotations object as an argument, which is an array of Annotation objects;
3. The function must return an object with the following interface:
```
{
    ok: boolean
    errorMessage?: string
    errors?: { [annotationId: string]: string }
}

```


### Debugging
To debug the validation script you can use your browser's Developer Tools while you are in the Annotation Studio tab. We recommend you use [Google Chrome](https://www.google.com/chrome/) if you want to do debugging. 

To go to your Developper tools and debug, make sure you are in the Annotation Studio, and then click the `Customize and control Google Chrome`(the 3 dots on the top right-side of your browser) -> `More Tools` and then click `Developer tools`.
***Note***: You can also press `Ctrl+Shift+I` to open the Developer tools pannel.

![image](https://user-images.githubusercontent.com/58508793/225914131-8260c8b9-614e-4355-9225-020acdc25c5f.png)



You can now use JavaScript debugging - ```console.log/debugger``` to see any error messages and issues that may occur with your script.

![image](https://user-images.githubusercontent.com/58508793/225915639-e996dd1c-d716-47a2-95aa-b7c32aee00ab.png)


To see coordinates of Annotations in the studio, which can help analyze the scripts behaviour, use the `_def` property.
![image](https://user-images.githubusercontent.com/58508793/225604778-900bce2b-614b-4431-858e-af6469fe008b.png)

### Annotation Object

When referring to Annotations received in the Annotations object, their properties comply with Dataloops' standard Annotation JSON format, which is [documented in full here](https://dataloop.ai/docs/annotation-json-format).


### Sample Validation Scripts
Here you can find a few sample Validation scripts that we made for you. As you will observe, the first one is the one we used ealrier. Feel free to use all of them as they are, or create your own.

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

Sample 3 - Bounding Box annotations must have a parent annotation
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

## Final Words

Dataloop has a lot of resources that can help you learn about the services we offer. However, it may be challenging to have a comprehensive understanding of the location of all resources or to locate something particular that you need. That's why we took care of organising all of them. 

Below, you will find links to a **mindmap** showing all of the resources available - each element is clickable and will redirect you to that resource. You will also find other Documentation pages and their descriptions, so you know where to look, and what you'll find.

1. [Dataloop's Developer Mindmap](https://gitmind.com/app/docs/m7u63dss) - a visual representation of all the resources available for developers.
2. [Dataloop's Developer Documentation on Redocly](https://developers.dataloop.ai/tutorials/tutorials/) - here you will find a [Beginner Onboarding](https://developers.dataloop.ai/onboarding/onboarding/) which will walk you throught the basics of using Dataloop's platform from the Python SDK, and also an [Advanced Onboarding Exercise](https://developers.dataloop.ai/onboarding/11_onboarding_exercise/) which will show you how to use the platform on a more complicated usecase; [you can also find them on GitHub](https://github.com/dataloop-ai/dtlpy-documentation), if that's your thing.
3. [Dataloop's Main GitHub Repository](https://github.com/dataloop-ai) - this repository contains the main dtlpy package, along with its documentation and other resources; this is meant to be a "clean" space containing the critical elements of Dataloop.
4. [Dataloop's Developer GitHub Repository](https://github.com/dataloop-ai-apps) - this repository contains resources, exercises, examples, documentations, etc. - its purpose is to be a Developer Community, which offers resources and guides from which developers can learn about the platform, ask questions and find useful code and guide that will solve their problems. 
5. [Dataloop's API Documentation](https://github.com/dataloop-ai-apps/dataloop-api-documentation) - this documentation is a beginner's guide to how to use Dataloop's Rest APIAPI ([click here to open the Swagger UI API page](https://gate.dataloop.ai/api/v1/docs/#/)); it will walk you through what API's are in general, what Dataloop's API is, how it helps you, why you should use it and teaches you **how** to use it. You can also [find a "Glossary" of all API commands here](https://github.com/dataloop-ai-apps/dataloop-api-documentation/blob/main/02_swagger_ui_api_guide.md).
6. [Dataloop's WebUI Version](https://console.dataloop.ai/welcome) - remember that you can always use (and should use) the WebUI version of Dataloop; some things are easier to do on the WebUI version, while others are easier to do in the PythonSDK version - so be sure to use both.

Finally, if you have any troubles in your journey to learn and use Dataloop, you can always contact us for help by clicking the small e-mail button located at the bottom right of the [main Dataloop web page](https://dataloop.ai/), or even [book a demo so we can walk you through how to use Dataloop](https://dataloop.ai/#talkToAnExpert).

