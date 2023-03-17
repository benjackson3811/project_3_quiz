# Testing

## Code Validation

The testing of [Cape Town Quiz](https://cape-town-quiz.herokuapp.com/) was done through [CI Python Linter](https://pep8ci.herokuapp.com/).
With each line of code, function writen and feature defined. The code was checked in the linter to solve the errors flagged. 
In addition frequent print statements were completed to ensure that the code worked and bugs found were solved. 

The Bugs found and how they were fixed are defined in the below section.

## Browser Compatibility 

Quiz tested on Google Chrome, Apple IOS, Microsoft Edge and Firefox with no errors found.

## Responsiveness Testing. 

Testing was completed on Am I responsive to show the quiz successfully responds to different screen sizes.
With each screen size rendering correctly.

![Am I Responsive](./readme.images/am-i-responsive.png)


## Bugs Found and fixed

1. 
- Bug: Error- Code to long 
- Found in code:  line 105
- Fixed How?:  Changed the naming of the lists being randomised. Logic taken from https://stackoverflow.com/questions/53158284/python-giving-a-e501-line-too-long-error

2. 
- Bug:  Final score % being calculated from un randomised list.
- Found in code : line 182.
- Fixed How?: Fixed updating the list the correct answer is taken from.

3. 
- Bug: Input validation - If incorrect selection is made (Not A,B,C,D) - user still able to go on to next question.
- Found in Code:  line 142.
- Fixed How? : Fixed by create separate function for the validation. 
Logic taken from Code Insitiute love sandwiches project. 

4. 
- Bug: Trailing WhiteSpace.
- Found in Code: At various points in the validation - error shown.
- Fixed How?: Fixed by checking stackoverflow and reapplying the recommendation to the code. https://stackoverflow.com/questions/21410075/what-is-trailing-whitespace-and-how-can-i-handle-this

5. 
- Bug: "Missing Docstrings warning" Pylint. 
- Found in code?. line 50.
- Fixed How?: Stack Overflow https://stackoverflow.com/questions/7877522/how-do-i-disable-missing-docstring-warnings-at-a-file-level-in-pylint 

[Unfixed Bugs](unfixed-bugs)

There are no known unfixed bugs.

## Input Validation

Each screen where the user inputs data has been tested. 

1. User makes a choice of whether to start the quiz, look at instructions or Quit Game.
- Possible validation errors:
    - User could input not 1,2 or 3
- Validation
    - if not 1,2,3 - the user advised its an invalid selection and is directed back to the choice. 
![Navigation Validation](./readme.images/navigation-validation.png)
</details><br />

2. Question Answer.
- Possible validation error:
    - user could input not A,B,C or D
    - user could enter a number.
- Validation. 
    - if not A,B,C or D the user advised its an invalid selection and is directed back to the choice. 
![Question Validation](./readme.images/question-validation.png)
</details><br />

3. Replay game.
- The user is asked "How about another game? - YES OR NO?" 
- Possible validation error
    - They could answer not YES or NO.
- Validation
    - if not YES or NO the user advised its an invalid selection and is directed back to the choice. 
![Replay Game Validation](./readme.images/replay-game-validation.png)
</details><br />

 ## Additional Testing

 As additional testing through Dev Tools a [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) report has been run. 

 The below aspects were tested. 
 - Performance - reveals how the site performs during loading
- Accessibility - shows if the site if accessible for all users and suggests ways to improve it
- Best Practices - indicates if the site conforms to industry best practices
- SEO - Search Engine Optimisation - shows if the site is optimised for search engine result rankings

### Results from Lighthouse

![Lighthouse test result](./readme.images/lighthouse-validation-testing.png)


