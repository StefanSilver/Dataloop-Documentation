# Annotations Validation

Annotation validation enables project managers to enforce almost any kind of Annotation rules. By loading a JavaScript file in the Annotation studio and running it when Annotators click on the Action button to assign an Item with a status, developers can build and enforce any kind of restrictions, such as:

- Labels that cannot co-exist (for example you cannot label both genders in an image with 1 person);
- Number of polygon points;
- Area or segmentation masks (avoid large masks);
- Minimum number of Labels required.

## Using Annotation Validation
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




You now need to locate the "Annotation Verification" section and click on the upload  button to select and upload your JS validation script file: 

![image](https://user-images.githubusercontent.com/58508793/225672898-70977ad7-0ab2-4ec7-b5f5-2b3d7d18ae50.png)


The file can be removed to allow changing versions, but only a single file can work in any recipe at a given time;

![image](https://user-images.githubusercontent.com/58508793/225602274-cf0772d5-180f-476e-9ac1-0048acbeb9ee.png)

3. [Create an annotation task](https://dataloop.ai/docs/create-task) that has this recipe as its instructions set;
4. When entering the annotation studio from the task/assignment, the JS file is loaded in the background, ready to be run;
5. Create annotations and press the actions button to set COMPLETED or any other status - the JS file is being executed;
6. As a user with Developer or Project-owner role, you will see a code-editor button, to open you JS file in code editor, edit it, and be able to run it.
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
