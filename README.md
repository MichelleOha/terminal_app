# MY WARDROBE Terminal App

MY WARDROBE is a terminal application that allows the user to enter in and store details about the items in their wardrobe so that they have a quick reference when they are shopping either online or in-store.

The user can enter new items, delete unwanted items, view their wardrobe and reset their wardrobe with this application.

Sizing varies so much across different brands and international sizes are different to Australia sizes.....When I shop for clothing or footwear online, I always find I have to run to my wardrobe and find an item of clothing from that particular brand so I can then go back to my order and select the correct size. The purpose of MY WARDROBE is to store that information for me in a json file so I have reference to is there and then, saving me time looking for it in my physical wardrobe.

# Repository:

https://Github.com/MichelleOha/terminal_app

# Implementation plan:

**Classes:**

A diagram of the classes that will be required for the application to work. These include:

1. Main class: runs the application.
2. InputOut class: the welcome_menu output for users selection and input. Also contains functions that define the input/output required for the app to work.
3. ReadWrite class: reads and writes to the json file.
4. Color class: used for text color in the application.

![classes](./docs/classes.jpg)

**Flowchart for MY WARDROBE:**

![flowchart](./docs/flowchart.jpg)

**PIP3 Installed packages:**

![Installed packages](./docs/pip3.jpg)

**Trello:**

![trello checklist](./docs/trello.jpg)

**Checklist:**

![trello checklist](./docs/checklist.jpg)

**Code style guide used** PEP8 which is one of the packages installed.

# Features

**Welcome_menu**

![Welcome Menu](./docs/welcome_menu.jpg)

-This features allows the user to make a selection from the options displayed in the welcome menu to navigate what function they would like to perform. Strings are colored for visual appeal.

**Storing of Data**

![Json file](./docs/json.jpg)

-The ReadWrite class has the responsibility of the persistance of data. In other words, the user reads and writes their items in the "wardrobe" which is the json file. As soon as the application runs, it reads the list.json file and checks for any data stored in there as a list. The json file allows us to store our wardrobe items, quit the application and reopen it and the data will still exist.

**Adding items**

![Input](./docs/adding_items.jpg)

- Option "1" in the welcome menu allows the user to add items to their wardrobe in this application. The user is asked six questions, one at a time so they can enter their input.

**Removing items**

![Remove items](./docs/remove.jpg)

- Option "2" in the welcome menu allow the user to remove items from their wardrobe in this application. The user is asked which item they would like to remove by title and the application then deletes it from the wardrobe (json file).

**View Wardrobe**

![View items](./docs/display.jpg)

-Option "3" allows the user to view there wardrobe. If there is any items in there they will be displayed. If not the welcome menu will be displayed.

**Reset Wardrobe**

![Reset the Wardrobe](./docs/reset.jpg)

- Option "4" allows the user to reset their wardrobe by deleting all existing items in the json file. They are asked if they are sure they want to reset the wardrobe. If Y, then the wardrobe is deleted. If N, the wardrobe is not cleared and remains as is. The string has been coloured in red and is bold to indicate a warning message before proceeding.

# How To Install MY WARDROBE

You must include:

- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application
