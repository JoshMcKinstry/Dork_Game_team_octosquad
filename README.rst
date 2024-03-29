Read Me
=======

Welcome to Dork! 

Dork is a text-based adventure game set in the year 2040 in MSU Denver.
It is a dark time for the university as a new Dean was initiated to the office.
The new Dean, while a good Dean, has been known for his hatred of birds.
This hatred is usually displayed through cruel acts like illegal hunting and capturing birds.
Recently, the dean has captured a Roadrunner and is planning to dispose of it 
regardless of the fact that the university's mascot is a Roadrunner. 

You play as a student of MSU Denver and upon discovering the Dean's evil plan,
you set out to free the Roadrunner from its cruel fate. 

* Free software: MIT license
* Documentation:

Requirements
------------ 
python 3.7.3
git

Pip packages 
------------
coverage
doc8
flake8
mock
pylint
pytest
pyyaml

Setup
-----
1. Open the terminal
2. Clone the game, type the following command at your terminal: git clone https://github.com/JoshMcKinstry/team34
3. Navigate to the direction of the team34 folder
4. Type the following command to start the game: python -m dork
5. Type the following command to run the tests: python -m pytest
6. Type the following command to install pip packages: pip install "Name of package"

How to Play
-----------
To play Dork, Players need to enter commands into the command line interface.
For example, to move north along the maze, the player would enter "move north".

These are the commands currently supported by the game*
*note: these commands are not case sensitive
- Help : Displays the list of commands.
- Move [Direction] : Moves to the room in the direction specified.
- Use [Item] on [Direction] : Use a key to unlock a door at the specified direction
- Open [Direction] with [Item] : Uses a key to unlock a door at the specified direction
- Take [Item] : Takes the item specified and stores it into the player's inventory.
- Drop [Item] : Drops the item specified into the current room.
- Examine [Item] : Displays the item description.
- Load : Loads a save file.
- Save : Saves the current state of the game.
- Quit : Exits the game to the main menu. You have the option to save the game before exiting
- Where : Displays the location of the player.
- Display : Displays the inventory of the player.

- [Directions] : north, south, east, west
- [Item] : cage, cellphone, dean-badge, donut, flower, flyer,
            freshman-badge, junior-badge, key, nest, paper, sophmore-badge

For a more in depth walkthrough of the game, refer to the "Game Design" folder in the team34 folder.

Credits
-------
* Josh McKinstry <jmckins3@msudenver.edu>
* Sinh Mai <smai2@msudenver.edu>
* Sky Liu <tliu1@msudenver.edu>
* Warren Joseph Ramos <wramos1@msudenver.edu> 
* Jacob Netwal <jnetwal@msudenver.edu>
* Andres Restrepo <arestre1@msudenver.edu>
* Rachel Rosebrook <rrosebro@msudenver.edu>
* Kevin Morales-Folgar <kmorale4@msudenver.edu>

Version: 1.0.0

This package was created with Cookiecutter_ and the
`lsmith-zenoscave/cookiecutter-simplemodule`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`lsmith-zenoscave/cookiecutter-simplemodule`: https://github.com/lsmith-zenoscave/cookiecutter-simplemodule
