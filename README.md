# Battleships Command

Battleships command is a python terminal game which runs in the Code Institute terminal on Heroku

Users can compete against the computer by correctly guessing the opponent's battleship coordinates before the computer finds theirs. The player can choose what board size and amount of ships they would like to use each game.

[Here is the live version of my project](https://battleships-command.herokuapp.com/)

![Responsive Mockup](/assets/media/mockup.png)

[Go to How to Play](#how-to-play)

[Go to Features](#features)
  - [Go to Existing Features](#existing-features)
  - [Go to Features Left to Implement](#features-left-to-implement)

[Go to Data Model](#data-model)

[Go to Testing](#testing)
  - [Go to Solved Bugs](#solved-bugs)
  - [Go to Remaining Bugs](#remaining-bugs)
  - [Go to Validator Testing](#validator-testing)

[Go to Deployment](#deployment)

[Go to Credits](#credits)

## How to Play

Battleship Command is based on the classic 'Battleship' game. You can learn more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this version, the player enters their name, choice of board size and number of ships for each player which then randomly generates two boards.

The player's ships can be seen, as indicated by a | sign, but cannot see the computer's ship coordinates.

Guesses are marked on the board with an X while hits are shown with an O.

The player can input a row and column to choose their next guess while the computer will randomly generate their choice, both attempting to find and sink each other's battleships.

The winner is the player who locates and sinks all of their opponent's battleships first.

## Features

### Existing Features

#### __Key Features__

 - Input validation and error-checking for all inputs

   - You cannot enter coordinates outside the size of the grid
   - You must enter a name for settings and and numbers for all relevant inputs
   - You cannot enter the same guess twice

 - Random generation

   - Ship coordinates and computer guesses are randomly generated within game settings parameters (shown below)

#### __Game Settings__

 - The game settings area accepts input for player name, board size selection and number of ships for each player.

 - This section provides the player with agency on how they would like to play and increases replay value.

![Game Settings](/assets/media/game_settings.png)

#### __Board & Scores__

 - The board & scores section displays player ship placements, current guesses and hits and provides a remaining ship count for each player based on game settings.

 - This section provides the player with visual indication of the current game state which is updated each round for guesses, hits and scores.

![Board & Scores](/assets/media/board_and_scores.png)

#### __Player Guesses__

 - This section shows the player's previous guesses, confirms if the player would like to continue and receives input for the row and column of their next guess.

 - This section fundamentally allows the player to control how they play the game and allows them to start again before the game ends naturally.

 ![Player Guesses](/assets/media/guesses_and_continue.png)
 ![Updated Board](/assets/media/updated_board.png)

### Features Left to Implement

 - Allow players to place ships themselves

 - Enable ships large than 1x1

## Data Model

In this project I decided to implement a `GameArea` class. This class stores variables and hosts methods for creating the boards, ship coordinates, player ship placement, updating guesses and hits and declaring the game over.

The `GameArea` class is initially fed arguments from the settings variable which changes based upon the selections chosen by the player. This then updates each round through the `new_round` function and the seperate functions it calls e.g. `new_guess` and `generate_boards`.

These functions and methods collectively game critical variables which are updated by function's `return` values and displayed to the player through `print` statements.

## Testing

I have manually tested this project by doing the following:

 - Passed the code through a PEP8 linter and confirmed there are no problems

 - Given invalid inputs: strings when numbers are expected, out of bounds inputs, same guess input multiple times

 - Tested in my local terminal and the Code Institute Heroku terminal

### __Solved Bugs__

 - When writing the project, the guesses and hit lists were resetting after each round. I fixed this by refactoring these lists as part of the `GameArea` class

 - When writing the project, errors were occuring once a non duplicate guess was input after a duplicate guess attempt was made. I fixed this by changing the value to `None` if a duplicate was identified then adding a `while` loop if the returned guess result was `None`

 - Tuples from guesses list fed in to `update_board` could not be unpacked. This was fixed by changing the `for` loop to `_, guess enumerate(guesses)`

### __Remaining Bugs__

 - Boards, scores, hit confirmation and previous guesses cannot all be displayed on screen at once for larger board sizes due to line count limitation on terminal

### __Validator Testing__

 - PEP8

   - No errors were returned from [PEP8online.com](http://pep8online.com/)

## Deployment 

This project was deployed using Code Institute's mock terminal for Heroku.

 - Steps for deployment:

   - Run command `heroku login -i`, then input login credentials
   - Run command `heroku create battleships-command`
   - In the Heroku app, set buildpacks to `heroku/python` and `heroku/nodejs`
     - Buildpacks must be in this exact order
   - Run command `git push heroku main`

 - Additional Notes:

   - Due to an ongoing issue, the GitHub deployment method for Heroku is currently unavailable

## Credits

 - README structure used from [Sample README.md - Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
 - Deployment terminal provided by [Code Institute](https://codeinstitute.net/)
 - Responsive design mockup tool by [Am I Responsive](https://ui.dev/amiresponsive)
 - Battleships game details by [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)
 - Seperate lists code by [User648852 - Stack Overflow](https://stackoverflow.com/questions/13443588/how-can-i-format-a-list-to-print-each-element-on-a-separate-line-in-python)

 [Go back to top](#battleships-command)