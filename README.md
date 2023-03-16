## [Portfolio_Project_3 --- Python_Essentials]

## Cape Town Quiz.

The project is a terminal based quiz game. The purpose of the quiz is to answer five questions at random and get a score. 
The Quiz is a terminal based interactive quiz where the user answers questions on Cape Towns History, South African land Animals and the Sea

Play the game here - https://cape-town-quiz.herokuapp.com/

## Table of Contents

[Table of Contents](#table-of-contents)

[How to Play](#how-to-play)
[Features](#features)
- [Front Screen](#Front Screen)
- [Display Menu](#display_menu)
- [Game_Instructions](#game_instructions)
- [New Game](#new_game)
- [Clear Screen](#clear_screen)
- [Check Answer](#check_answer)
- [Display Score](#display_score)
- [Play Again](#play-again)
- [system_exit](#system_exit)

[Data-Model](#data-model)

[Features Left to Implement](#features-left-to-implement)

[Credits](#credits)

[Testing](#testing)
- [Bugs Found and Fixed](#bugs-found-and-fixed)
- [Unresolved Bugs](#unresolved-bugs)

[Technologies Used](#technologies-used)

[Deployment](#deployment)

[Game Link](#game-link)

[Cloning of the project](#cloning-of-the-project)

[Acknowledgements](#acknowledgements)

[Back to Top](#table-of-contents)

<hr>

## How to Play

You will answer five questions!- They will be a mixture of three topics

 1: Cape Town History
 2: The Sea. 
 3: South African Land Answers

 Each question has four options, A, B, C or D

 If your answer is correct, the system will tell you! 

## Features

* front screen
* Display Menu
* Game Instruction
* Clear Screen
* New Game
* Check Answer
* Display Score
* Play Again
* sys.exit

[Back to Top](#table-of-contents)

## Data Model
Link to game flow chart

[Back to Top](#table-of-contents)

## Features Left to Implement
- Highscore - to allow the player to gain a log of their previous games. This would allow a username to be added.
- Multiple Topics 

## Credits
Bro Code youtube video on building a python based quiz game. - https://www.youtube.com/watch?v=yriw5Zh406s.
Used as an initial guide on simple structure. The inital code for functions new_game(), check_answer(), display_score() and replay_game() was taken from here.

Quiz functionality
BroCode youtube Video. https://www.youtube.com/watch?v=zehwgTB0vV8&t=188s.
Used as guide on how to build a python quiz.

https://realpython.com/python-quiz-application/#step-2-make-your-application-user-friendly

- logic on how to clear a screen in Python
https://www.scaler.com/topics/how-to-clear-screen-in-python/

- logic on how to quit a quiz. For the quit game funcgiton.
https://stackoverflow.com/questions/58913904/how-to-quit-on-a-python-quiz



## Testing

Testing completed. 
1) Tested on CI Python Linter with one error found - too long code. 
2) Tested validations to confirm only correct inputs are counted in confirming the final score. If incorrect selection is made (Not A,B,C,D - no score is added to final score.
3) Tested in Local terminal and the code institue Heroku terminal


Bugs Found and fixed
https://stackoverflow.com/questions/19895028/randomly-shuffling-a-dictionary-in-python

https://stackoverflow.com/questions/71838278/attribute-error-list-object-has-no-attribute-get

[Back to Top](#table-of-contents)

Unresolved Bugs
to long code - error on linter

## Technologies Used.

- Github - https://github.com. To Edit and Deploy thw website.
- Gitpod - https://gitpod.io/projects- To deploy and create the website.
- Heroku- https://www.heroku.com - To deploy the game into a mock terminal that allow the game to be played online.
- Python- https://www.python.org/ - To produce and run the app.
- NodeJs - https://nodejs.org/en- To produce and run the app.
- CI Python Linter https://pep8ci.herokuapp.com/ - To define errors
- Trello - https://trello.com/ - to manage project manage my ideas.
- Stack Overflow - https://stackoverflow.com/ - to find dedug and find solutions to my questions. 
- Real Python.com https://realpython.com/- to find dedug and find solutions to my questions.

### Deployment.
I deployed the game using Heroku, a cloud based container platform. This platform is specifically designed to deploy, manage and scale applications.

The below steps were followed.
1) Create an app on Heroku.
2) Ensure the Heroku student credits were successfully applied.
3) On Dashboard. Click New. Then create new app.
4) Navigate to Settings section.
5) Click Config Var.
6) Add Config Var.
- Key: PORT.
- Value: 800.
7) Click Buildpacks.
- add Buildpacks for python and nodejs. This is to link the app to these softwares.
8) Navigation Bar - Deploy.
9) Deployment Method - click Github
- add name of repository into search bar for Heroku to search for.
10) Deploys.
- Click Automatic or Manual Deploy 

[Back to Top](#table-of-contents)

### Game Link
https://cape-town-quiz.herokuapp.com/

[Back to Top](#table-of-contents)

### Cloning of the Project.

To create a local clone of the project, please follow the below steps.
- In the GitHub repository, under the repository name there is a code tab., click on the code
  - In the clone tab, click the HTTPS tab. Within this section, click on the clipboard icon and copy the URL supplied for the repository.
  - Open an IDE of your choosing and run Git Bash.
  - Change the current working directory to the location of which you wish to place the cloned repository.
  - In the terminal, write Git Clone and then paste in the URL supplied via GitHub from step 2.
  - Press enter and your new cloned repository will be created within the desired location.
  
[Back to Top](#table-of-contents)

### Acknowledgements

With my 3rd portfolio Project, i would like to thank my mentor Precious, for his feedback, guidance and patience to help map and improve my idea in the project. 
I would also like to thank the tutor support team with their help to debug my ideas into solutions.
