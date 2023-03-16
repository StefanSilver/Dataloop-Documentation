# Annotations Validation

Annotations validation enables project managers to enforce almost any kind of annotation rules. By loading a JavaScript file in the annotation studio and running it when annotators click on the Action button to assign the item with a status, developers can build and enforce any kind of restrictions, such as:

- Labels that cannot co-exist (for example you cannot label both genders in an image with 1 person)
- Number of polygon points
- Area or segmentation masks (avoid large masks)
- Minimum number of labels required

## Using Annotations Validation

1. Open the recipe and change to the Instructions tab
2. Locate the "Annotation Verification" section and click on upload to select and upload your JS validation script file. The file can be removed to allow changing versions, but only a single file can work in any recipe at a given time;

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
