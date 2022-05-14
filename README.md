# To the moon and back

## Introduction
To the moon and back is a browser-based game build in Python. It is based on a classic game of traveling and is themed loosely around traveling to the moon, researching it and returning to back to the earth. 
As the game was developed in python for use in the terminal, it utilises the Code Institute Python Template to generate a “terminal” onto the page, making it available within a web browser.

![Screenshot 2022-05-14 154938](https://user-images.githubusercontent.com/96884287/168430861-01f6d8f4-b21b-4985-ba17-2655b6fbb7ce.png)


The game has been deployed via heroku and this can be found here. **(Add link of deployed game)**

*Please note: To open any links in this document in a new browser tab, please press CTRL + Click.*

## UX

### The strategy Plane

To The Moon and Back, intended to be a fun game where the user has been selected to take part in a journey to the moon and back. 
The adventure is starting right when the user will run the terminal. 
This type of game can be played for short or medium periods of time, as the user has the chance to train a longer period before getting the chance in real life to travel to the moon.
Given the limitations of the terminal-based interface, care will need to be taken to incorporate visual stimulus, along with an engaging narrative to convey an element of fun to the user.


### Site Goals

-	To provide users with fun and a simple traveling game to play.
-	To provide the user the ‘necessary training’ before traveling to the moon.
-	To provoke the user to win the game as there are multiple chances to lose and just one chance to win the game.

### User Stories

-	As a user I want an online version of traveling to the moon.
-	As a user I want to be able to control the amount of time it takes to play the game.
-	As a user I enjoy challenges and keeping in mind that there is just a chance to win this can be very challenging sometimes. 

## The scope Plane

### Features planned

-	As there are certain restrictions in the scope of the development of the application, such as the terminal confines and methods of deployment. It will be important to ensure all functionality is contained within the game terminal screen.
-	Despite the confines of the terminal emulator, the site should site be visually stimulating and clear to the user that it is a game.
-	The game has just one chance to be one and this has been implemented to challenge to user to play the game, offering him a feeling of victory at the end of the game when this will win.


## The structure Plane

### User story:

As a user, I want a fun and simple game to play.

Acceptance Criteria:

-	It should be clear to the user that this is a game, what it is about and how to play.

Implementation:

-	The layout, use of colour and in game narrative will all be designed to immerse the user into the game world. Conveying a sense of fun to the user throughout the interactions with the game. Instructions on how to play will be available at the start of the game, along with clear prompts and validation for each user input.


### User story:

As a user I want to be able to control the amount of time it takes to play the game.

Acceptance Criteria:

-	The user should be able to control the amount of time it takes to play a game.

Implementation:

-	The user will be challenged to continue the game until the end however, if he decided that he want to exit the game he can do this choosing a wrong variant, this game system has been implemented to challenge a part of users to play the game until they will win, as there are multiple variants of losing the game and just one to win the game. 

### User story: 

As a user I enjoy challenges and keeping in mind that there is just a chance to win this can be very challenging sometimes.

Acceptance Criteria:

-	The user should have the option to play the game and feel challenged by this game.  

Implementation:

-	The user will be challenged to play this game until he will win, the game is very simple, and the idea of this game is to challenge the user directly, offering him only one chance to win the game and multiple chances to lose. 


**Opportunities**                        |                 *Importance*         |        *Viability / Feasibility*
“Provide a fun game environment          |                      5               |                  5
“Provide a challenging game              |                      5               |                  5


## The skeleton planes

### Wireframe mock-up

Given that the application will be run within a terminal emulator provided within the template, there are limited options available with regards to the layout of the webpage itself. And I decided to leave simple and elegant. 


![Screenshot 2022-05-14 160400](https://user-images.githubusercontent.com/96884287/168432485-874d8278-fb46-4e88-b7fc-efb8d586638c.png)



## Logic Flow

To develop the logical steps required within the game, along with gaining an understanding of how the different game elements would interact, I created a flow chart detailing the individual steps for the game. Given the scope of the game logic involved the full flow chart resulted in a large image.


1. ![chart 1](https://user-images.githubusercontent.com/96884287/168432592-cb3d8337-56d7-4983-9ae4-ee5c127b597e.png)


2. ![chart 2](https://user-images.githubusercontent.com/96884287/168432617-ee713efe-bf58-4246-accb-d370629fe6a3.png)



## Features

Welcome Screen

The user will receive instructions in the beginning of the game introducing him to how the game works, what is this game, and what he will need to do.

![Screenshot 2022-05-14 160605](https://user-images.githubusercontent.com/96884287/168432822-327ab67b-f137-4f0a-9b98-a9694531d3ed.png)


When the user will start the game, he will be directed into the game and the story line will start explaining and introducing the user to the flow of the game, after the first part of the story line the logo of "To the moon and back" will appear in a blue colour. 
  
Game Start Screen

Immediately after the story line, the game will begin asking for the user input, if they would like to proceed the game will begin, if they will change their mind they can end the game by saying ‘no’. 

![ws](https://user-images.githubusercontent.com/96884287/168433095-15996838-8203-4d1d-890b-045ef5a913d9.png)

Throughout the game

The user will be exposed to different situations where his input will be required to fallow the flow of the story. In this part of the game, the user can lose the game very quickly or win it. Now depends on their instincts.

End Game Screen

Once the user (or the AI) has completed with success the game, they can see a message ‘’Winner’’ showed up on the screen, if the user loses the game, the ‘’Game Over’’ message will be on the screen and they will requested the user input to try again or leave the game. 

-	Winner

![Screenshot 2022-05-14 161248](https://user-images.githubusercontent.com/96884287/168434019-3d5f4d0d-577b-4b10-af9e-b0d07cb7f542.png)


-	Game Over 

![Screenshot 2022-05-14 160952](https://user-images.githubusercontent.com/96884287/168433491-b60fb5ed-4d96-4a06-827f-d8f3b65cd1f3.png)


### Testing Strategy

I took a two-stage approach to testing the game. The first stage was continuous testing as the application while was being developed. With the application being based within the terminal, it was straight forward to test functions and print statements as they were being developed using the terminal within the IDE. During this stage of testing multiple tests were conducted to ensure that all the sections are fully responsive and there are no issues running the game. 

### Steps:

1.	Testing introduction()


I have started my testing with the introduction() function, making sure it correctly displays the beginning of the story and that time.sleep() delays the printing of following sentences as planned (the default timing has been set to 2 seconds but is changed to 4 in certain parts of the game for dramatic effect).

This function and all its elements work as expected and no bugs appear.


2.	Testing start_game()

In this function, player is asked whether they would like to play or not (“The Chief engineer requested you to join a mission to the moon! Are you ready for the lifetime journey?! (yes/no): ).

When I inputted "yes" into the terminal, the game continued correctly and the get_username() function was called next as expected.

When I inputted "no" into the terminal, the game displayed a Game Over message and the play_again() function was called as expected, allowing me to start again.

When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.

Conclusion: This function and all its elements work as expected and no bugs appear.


3.	Testing get_username()

In this function, player is asked to provide a username (What is your name, young astronaut? (type name): ).
They can input anything but a blank input.
When I inputted my name or any other word / character, an f-string was correctly printed with the chosen value ("What a great name! Welcome to your life trip, {name}!") And the game then proceeded correctly with the next part of the story.

When I tried to submit an empty input by not typing anything in and just pressing Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.

After inputting the username, the function continued with the story until I was asked if the landing procedures have been followed ([“…(Have you followed the landing procedures? (yes/no): )]).

When I chose "yes", function choice_two() was called as expected.

When I chose "no", function play_again() was called as expected.

When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.


Conclusion: This function and all its elements work as expected and no bugs appear.


4.	Testing choice_two()

In this function, the user is asked whether they would like to pick up a gun they find in on the surface of the moon. ("Do you take the gun? (yes/no): ").                                                                                                                                                                                                     
When I typed "yes", the game moved to the next part of the story, choice_of_three(), as expected.
When I typed "no", the game ended with the alien coughing the user, as expected.


When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected.

Conclusion: This function and all its elements work as expected and no bugs appear.

5.	Testing choice_of_three()


When this function is called, the player will be requested to input his next move this being (stay/hide/run), in these choices the game has hidden the right answer and the other answers will lead to a dead end. 

To test this is true, I have started the game again and again, conducting the checks, if the variant ‘stay’ has been chosen the game will end as expected. If the variant ‘run’ will be chosen the game will end as expected, and play_again() definition will be called. When the user will choose ‘hide’ the game will continue with crew_assist() moving forward through the game. 


When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 


Conclusion: This function and all its elements work as expected and no bugs appear.


6.	Testing crew_assist():

When this function will be called, the player will be calling for help from his crew mates, and he will need to choose if he prefers to continue the research or return to the spaceship.

If the user chooses return, the story continues until a point where he hears a cracking in his costume, and the game ends. And the function play_again() will be called as expected.

If the user chooses to continue, the crew member will be alerted that he needs a new oxygen tank. And the function do_research() will be called in order for the user to continue the game researching the surface of the moon. 


When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 

Conclusion: This function and all its elements work as expected and no bugs appear.


7.	Testing do_research()

Whilst the user is conducting its research on the surface of the moon, the crew mate meets an alien and he is killed, immediately after, the user is informed and he has to choose what he will do next, he can choose if he will continue his research or he will return back to the spaceship, in order to create more suspense the user will be informed that he has just 25% oxygen left.  The user will need to choose what he will do next, returning to the spaceship or continue its research. 

If the user will choose to continue, an appreciation message will be showed and he will continue researching until his oxygen is running out and he is falling down unconsciously and he die, a message saying game over will be presented and the play_again function will ask the user if he will like to try again. 

If the user will choose to return, the returning_to_the_spaceship() function will come in and the user will move further into the game. The game is running with no errors and the user will be send to the next chapter. 


When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 

Conclusion: This function and all its elements work as expected and no bugs appear.


8.	Testing returning_to_the_spaceship(): 

When this function is called, the player encounters an alien and is presented with two different options of what they can do in order to try to survive the encounter. 

The first option is to hide from this creature and try to protect himself. The second option is to kill the alien and take his body back to earth. The user can use the gun found previously on the moon surface to kill the alien. To test this is true, I have started the game again. Once I encountered the alien, I expected to see 2 choices and I did, meaning the code works properly. After making sure the proper choices appear, I than proceeded with testing the code: When I chose "1" (hide yourself), the game led to a Game Over scenario and the play_again() function was called as expected, allowing me to start again. When I chose "2" (Kill the alien), function back_to_earth() was called as expected. 

Note that the above choices require an input of an integer for which reason there are two different errors displaying if input is incorrect. First error notification: when I tried submitting an empty space or a non-integer character, the ValueError option kicked in, informing me of the wrong input and that the correct one must be a number. This works as expected. Second error notification: When I tried submitting a number that isn't the required 1 or 2, I received another error message informing me of the wrong input and that the right one can only be 1 or 2. 
This works as expected.

When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 


Conclusion: This function and all its elements work as expected and no bugs appear.


9.	Testing back_to_earth()

The storyline towards the end of the game, is exposing the user to the last challenge where he will need to choose if he would like to repair or not the spaceship before departing from the moon towards earth. 

If the user will choose to ‘fly’ with the spaceship damaged, he will lose the game. A message will be printed and the play_again() function will be called where the user can choose if he prefer to start a new game or leave.

If the user chooses to repair the spaceship before departing, the end of the game will be printed and user will ask what he prefer to do next, to leave or PlayAgain. 
If the user prefers to leave a goodbye message will be showed. If the user prefers to play again, the message (“That's a good choice, more training before the real thing! “) and the function play_again will be called. 


When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect and asking for the correct input again, as expected. 


Conclusion: This function and all its elements work as expected and no bugs appear.


10.	Testing play_again()

This function is called every time a player loses or wins a scenario, and it allows to load the game again ("Are you ready to try again? (yes/no)").

When I typed "yes" into the terminal, the function introduction() was called and the game started again, as expected.

When I typed "no", I was presented with “That’s not what we expected... Thank you for playing!" and wasn't asked again, as expected.


When I inputted other, unexpected words / characters or just left the input blank and pressed Enter, the while loop kicked in, informing me that the input is incorrect 
and asking for the correct input again, as expected.


Conclusion: This function and all its elements work as expected and no bugs appear.


## Validator Testing

pep8online.com - I utilised pep8online.com to validate my python code. All python files were checked with no errors reported.
Screenshots of the validator reports are here:

![Screenshot 2022-05-14 155018](https://user-images.githubusercontent.com/96884287/168434866-56f56d04-4a82-46fa-b5ae-6f248d0f63c7.png)



## Libraries Utilised


Built in Python Libraries

Several of the built-in python libraries were utilised to enable additional functionality within the application.

Python was used as the programming language to make the game.

LucidChart was used to create the flow chart showing the game's logic.

GitHub has been used to store the code, images, and other content.

Heroku was used to deploy the game to the web.

Git was used to track changes made to the project and to commit and push code to the repository.

Python module time has been used to allow for a delay between lines of text displaying.

Python module sys has been used to print a string of text character by character instead of all at one.

Colorama has been used to add a colour to the output in the terminal to create an effect of difference to the user.

Pyfiglet has been used to add a different text to the ‘game over’ and ‘winner’ so the user distinguishes the winning or game over message from the other text. 


## Deployment


The site was deployed via Heroku, and the live link can be found here – add link

The project was developed utilising a Code Institute provided template. 

To deploy the project through Heroku I followed these steps:

Sign up / Log in to Heroku

From the main Heroku Dashboard page select 'New' and then 'Create New App'

Give the project a name - I entered ADD and select a suitable region, then select create app. The name for the app must be unique.

This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.

This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might 
not need to add a config var.

In the config vars section select the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.

In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.

Next select the add build pack button below the config vars section.

In the pop-up window select Python as your first build pack and select save changes.

Then repeat the steps to add a node.js build pack.

The order of the build packs is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.

Next navigate back to the deploy tab using the submenu at the top of the page.

In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account

In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository and select search.

Once Heroku has located the repo select connect.

This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.

In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button

This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilise the manual deployment options further down. For this project I utilised the Automatic Deployment to enable me to check changes I made to the app as I developed it.

Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.


## Credits

The mock terminal used to host the game has been created by [Code institute.](https://learn.codeinstitute.net/login?next=/dashboard)

The code is custom and written entirely by me and the story is of my own idea.

Pyfiglet has been installed and used from [here.] (https://pypi.org/project/pyfiglet/0.7/)

Colorama has been installed and used as instructed from [here.](https://pypi.org/project/colorama/)

The game logo has been created by me in a Notepad file. 

The sys and time functions have been used as instructed in [here](https://www.programiz.com/python-programming/time/sleep)



## Acknowledgements

I'd like to thank the following:

My mentor Daisy McGirr for encouraging me throughout the project.

To Code Institute for teaching me how to use python.
