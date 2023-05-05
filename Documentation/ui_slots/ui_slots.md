# UI Slots

## What is an UI Slot?

A UI Slot is extremely useful because it lets you add your own customized function to the platform's interface. Once added, you can call it at any time you want with just one click. Once a UI Slot is activated, users can execute the function using the UI Slot in the Dataset browser, Task browser, or Annotation Studio.

This short guide will teach you how to add UI Slots in Dataloop's web UI.

Before you learn how to add a UI Slot, it's mandatory that you [learn How to Load FAAS Via Web-UI](https://github.com/dataloop-ai-apps/load-faas-via-web-ui). So go through that tutorial, and then come back and learn how to add UI Slots in Dataloop. We will also present a short version of creating the required codebase file in the next section (Creating FaaS Package), if you want to take a shortcut.

**Note:** If you want to add to your FaaS as an UI Slots, you will need to do it when creating the FaaS; however, you can also do it by editing an existing function.

## Creating FaaS Package

The first step, before creating an US Slot, will be to create a FaaS Package. Our Package consists of a Python module in .py format that has a class and a single function, that we will later compress as a `.zip` file. Let's take a closer look at an example of how to create this.

Open a Python IDE of your liking and create a new Python file called `main.py` that will contain our class and function.

Import our `dtlpy` library and create a `ServiceRunner` class; inside this class we create a function called `clone_item_five_times` that will execute our script.
```python
import dtlpy as dl
class ServiceRunner(dl.BaseServiceRunner):
    @staticmethod
    def clone_item_five_times(item: dl.Item):
        for i in range(5):
            item.clone(dst_dataset_id=item.dataset_id,
                       remote_filepath="/{}.png".format(i),
                       with_metadata=True,
                       with_task_annotations_status=False,
                       with_annotations=False,
                       allow_many=True)
```
After doing this, you need to save your python file, and then archive it to .zip file so that we can upload it to our platform. Make sure the file is `.zip` and not `.rar` or anything else, to be able to upload it.

![image](https://user-images.githubusercontent.com/58508793/236432294-24060a78-ad08-49af-8611-a46a2240f31a.png)

Also create a requirements.txt file, where you place each external library that you require to run your codebase. Place one library on each line, as seen below.

![image](https://user-images.githubusercontent.com/58508793/236442993-c8483669-5f22-46a8-ad98-1c612aae18a0.png)


## Adding an UI Slot

Before you can add a UI Slot, you need to go to the Application Hub in Dataloop's Web UI. To do that, you need to go to the left side of the screen, and click the `Application (FAAS)` drop-down button. There you will find the Application Hub. Click on it.

![image](https://user-images.githubusercontent.com/58508793/236271605-68c8bd3e-4dc0-448e-b0b2-05812280c993.png)


Let's now get into how to actually add a UI slot. To successfully add a UI Slot, you need to follow these steps:
1. First, you need to click the `ADD FUNCTION` button. Now you need to `Select Codebase`, which will open a search tab - look for your `.zip` file containing your functin and add it here. If you have any requirements (other Python Libraries) add them as a text file, mentioning each library on a new line and then add it to `Upload Requrements.txt` ([see How to Load FAAS Via Web-UI](https://github.com/dataloop-ai-apps/load-faas-via-web-ui) for more information). You can then go and pick an Input. In our example we will pick an Item, by clicking the little `+` button at the bottom of the page . Then click `CREATE`. Without this action, you won’t be able to create UI Slots, so make sure that you do it right. See an example below.

![image](https://user-images.githubusercontent.com/58508793/236434293-2449597d-46b1-4114-bd51-69571a232cc2.png)

2. Click the three dots in your function and choose “Add UI Slot”.

![image](https://user-images.githubusercontent.com/58508793/236434708-bfc91dd6-d336-495b-b754-831a531c3e98.png)


3. Click `ADD NEW SLOT`, pick a module name, a function name, and a display name and press `OK`. In our case resource type is Item as we defined it when creating FaaS. The panel is the place from which you will be able to call your function, in this case `studio` which means the Annotation Studio.

![image](https://user-images.githubusercontent.com/58508793/236268254-a4ec6c47-2f3b-49a0-a221-65333d040716.png)

4. You need to Install the new FaaS Function (just press Install and then Install again on the pop-up). This will transform the Package you just created into a Service that you can use from the UI Slot you just created. See below how to install it.

![image](https://user-images.githubusercontent.com/58508793/236438676-28e7164d-5d03-430e-a259-c1219fb20242.png)

5. After installing the Service, the next step is to actually activate the UI Slot for your Project. To do that, click the 3 dots on the right-side of your Service, and click `Activate UI Slots`.

![image](https://user-images.githubusercontent.com/58508793/236440962-09135b16-6680-420f-b7c8-a5455aa15c1d.png)

And then select the Project you want to add the UI Slot to, and press `APPLY`.

![image](https://user-images.githubusercontent.com/58508793/236441158-03b83197-bb2e-4864-91c5-c2633d00c490.png)

A pop-up should appear, letting you know that the UI slot was successfully added.

## Using the UI Slot
Now that the FaaS function was created and installed, we can go and test the new UI Slot in the Annotation Studio. To do that, go to the left-side of your screen, and under `Data Management` click `Datasets`. This will open all of your Dataaset from the current Project.

![image](https://user-images.githubusercontent.com/58508793/236439938-1bb2f6a8-e9f6-41f2-af94-e07f795fb537.png)

Now, just double click the Dataset you want to test the new UI slot on. The Annotation Studio will open up.

![image](https://user-images.githubusercontent.com/58508793/236440135-46fe9854-bb3f-4125-93b8-9ba8e814d348.png)

Now, double click and Item, to open it up and click the little robot head on the left-side of the screen.

![image](https://user-images.githubusercontent.com/58508793/236441455-69d60832-5b92-45ed-b2ab-c2cb76458c84.png)


By clicking that little robot head, you will be able to select a Function to use. Here, you will also see the Service you just created, as an UI Slot. Select it and `RUN` it to test.

![image](https://user-images.githubusercontent.com/58508793/236441891-95b8a0f0-60a2-42f0-a1d2-932d785daddd.png)

If the Service Function was executed successfully, you will see a pop-up letting you know the function ran successfully.

![image](https://user-images.githubusercontent.com/58508793/236442677-65add811-9a76-433b-a967-b35977193a8b.png)




## Places where you can add UI Slots
There are 4 spots in the platform interface where you can call your function manually.
For Datasets - Panel in Dataset Browse
For Items - Annotation Studio
For Tasks - Task Browser
For Annotations - Annotation Studio

Dataset
![image](https://user-images.githubusercontent.com/58508793/236268346-c9d98696-d492-4e6c-89e4-520ba05001f1.png)
![image](https://user-images.githubusercontent.com/58508793/236268385-75302228-501a-46be-a0e9-afd51cabe658.png)



Item

![image](https://user-images.githubusercontent.com/58508793/236268444-bf7e22c5-3591-4004-aec1-10ee774970bf.png)
![image](https://user-images.githubusercontent.com/58508793/236268484-817dfb23-9422-4c29-a380-e02f1f578301.png)


Task
![image](https://user-images.githubusercontent.com/58508793/236268543-23eb8c2b-2997-498a-9ce2-d90e5fee1add.png)
![image](https://user-images.githubusercontent.com/58508793/236268585-43258fb6-6751-407f-828f-80cb222f5f00.png)



Annotation
![image](https://user-images.githubusercontent.com/58508793/236268716-7075fc79-d99f-4da6-b77e-ad51be4d3d52.png)
![image](https://user-images.githubusercontent.com/58508793/236268772-f35d6217-3a9a-496f-939a-e3d15b1cbeff.png)




