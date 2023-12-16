# Connect 4 Game Documentation

## Table of Contents

1. [Introduction](#introduction)
    * [Demo](#demo)
  
2. [Features](#features)

3. [Objectives](#objectives)
    * [Developer's goal](#developers-goal)
    * [User's goal](#users-goal)

4. [Getting Started](#getting-started)
    * [Technologies used](#technologies-used)
        - [Language](#language)
        - [Toolchain](#toolchain)
        - [Necessary imports](#necessary-imports)
    * [Prerequisites and Deployment](#prerequisites-and-deployment)
        - [Installation](#installation)
        - [Local Development](#local-development)
        - [Deploying on Heroku](#deploying-on-heroku)
            - [Essential when creating the Heroku app](#Essentials)
        - [Constraints](#constraints)
5. [Testing](#testing)
6. [Acknowledgements](#acknowledgements)
7. [Future Features](#future-features)
## Introduction

Connect 4 is a classic two-player connection game where players choose a colour and take turns dropping coloured discs into a grid. The objective is to connect four discs in a row before your opponent does.

### Demo

- [Live Site on Heroku](https://connect-4-pp3-f3bf4c65e965.herokuapp.com/)
- [GitHub Repo](https://github.com/JonFD4/Connect4.git)
---

## Features 

- Text-based interface for easy gameplay.
  - Clean and intuitive user interface.
- Two-player mode or user vs. computer.
- Interactive grid for dropping pieces.
- Win detection for vertical, horizontal, and diagonal connections.
- Clear prompts and visual feedback for an intuitive user experience.
&nbsp;
---
### Objectives

#### Developer's goal
**Design**

![Lucid chart planning of game](assets/images/Connect-4-planning.png)
[Lucid chart planning of game](assets/images/Connect-4-planning.png)
1. *Game Logic Implementation*
   - Develop the core game logic, including rules and turn handling.
2. *User Experience*
   - Create a clean console interface with clear prompts and visual feedback.
3. *Python Skill Development*
   - Provide an opportunity to implement and develop Python skills.

#### User's goal

- Play an online game of logic and strategy.
- Choose between computer and another user.
- Identify owned and opponent pieces visually.
- Experience interactive gameplay.
- Exit the game prematurely if needed.
- Know the results at the end of the game.
- Have the option to play again.
---
### Product Features
&nbsp;

![title page](assets/Connect4features/intro-page.png)
    *Title and introduction page* <br>
The 'landing page' used pyfiglet to design an ASCII art of 'Connect 4'.
There are 3 options provided: the choice of playing with person, computer or simply exiting.
Underneath is the input that requests user to make a choice.
<br>
<br>

![rules page](assets/Connect4features/Rules-page.png)

*Rules page* <br>
Immediately on entering selection, the rules of game are displayed in a list on screen. The slighty different changes depending on whether user is playing with computer or another person.
<br>
<br>

![initial board](assets/Connect4features/initial-board.png)

*Initial board* <br>
A free board is printed out. At the top is a text that informs user of who they are playing with. A prompt also request user to chose a column.
The columns and the rows are labelled to make it readable and easy for players to choose.
<br>
<br>

![first-turns](assets/Connect4features/first-piece-drops.png)
*Turns and color + number representation* <br>
In the user vs user play, when each player takes their turn, a piece which is a number with a background color is printed (1/yellow and 2/blue). 
There are slightly different features if it is user vs computer play. "Computer is thinking..." which gives the illusion that computer is taking its time to play. Of course, this delayed response is implemented using the time module.
Each turn shows what decision a player made.
<br>
<br>

![final piece](assets/Connect4features/finalgameboard.png)

*Final piece* <br>
The final board shows a beautiful display of blues and yellows and choices that have been made.
Underneath it is an output that informs who won. This is followed by the `play again` query.

---
<br>
<br>

**Input, Input validation, and Error handling**
<br>
<br>

![start choice](assets/Connect4features/start-choice-error-handling.png)
*Start choice error handling* <br>
The user is immediately prompted if the input is invalid. A message is displayed to inform of wrong input, followed by another input asking for the correct input choices.
<br>
<br>

![column-choice error handling](assets/Connect4features/error-column-message.png)
*Wrong column input* <br>
Immediately, a response informing user of wrong input, followed by request for input is output for user.
<br>
<br>

![play again validation](assets/Connect4features/play-again-validation.png)

*Play again validation*  
play agian feature requests either `yes` or `no`. If it is `yes`, the game restarts, displaying the landing page and game mode choices.
<br>
<br>

![play again error handling](assets/Connect4features/play-again-error-handling.png)
*play again error handlin* <br>
If user inputs the wrong data, the prompt is set up to keep asking until user inserts either `yes` or `no`. 

---
<br>

<h3>Exit Strategies</h3>
<br>

![early exit](assets/Connect4features/premature-exit.png)
*Early exit* <br>
This is the third option that is presented when user is choosing a column. `0` allows user to exit befire game ends. 
Additionally, this feature is beneficial during early development when developer wants to make certain test without having to complete the game. `Exiting the game. Goodbye!` is the message output.


![play again exit](assets/Connect4features/play-again-exit.png)
*play again exit* <br>
This removes user from the game completely and outputs a message `Thanks for playing! Exiting...`

---
<br>

# Getting Started

## Technologies Used
### Language
- Python

###  Toolchain
- Lucid chart
- Visual Studio Code - IDE for code development
- GitHub - Version control and repository hosting
- Heroku - Deployment and hosting

### Necessary Imports:
- Colorama: A Python library for adding colored output to terminal text.
- pyfiglet: A Python library for creating ASCII art from text.
- numpy: A powerful library for numerical operations in Python.
- sys: Provides access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter.
numbers.
- string: Provides common string operations.
- time: Provides functions to work with time.
- textwrap: Provides convenient functions for formatting text.
---

## Prerequisites and Deployment

The game was developed in VS Code, stored in GitHub as the local repository, and deployed on Heroku.

### Installation

- Ensure [Python](https://www.python.org/) is installed on your system.
  ```bash
  python --version
  # or
  import sys
  print("Python Version:")
  print(sys.version)
  print("Python Version Info:")
  print(sys.version_info)
  ```
- Depending on Python version, use either `pip` or `pip3` to install libraries and modules.
  ```bash
  pip3 install random
  ```
---
### Local Development

**Fork the Repository:**
1. Login to GitHub or create a new account.
2. Find the repository of interest.
3. Click on `Fork` in the top right corner.

**Cloning a Repository:**
1. Find the repository of interest.
2. Click the `Code` button in green and select `local`.
3. Click the `copy` button beside the repository link under `HTTP`.
4. In your local IDE, select git clone and paste the link, then select the directory you want it stored in.

Alternatively (Via terminal):
1. Clone the repository.
   ```bash
   git clone https://github.com/JonFD4/Connect4.git
   ```
2. Navigate to the project directory.
   ```bash
   cd connect-4
   ```
3. Run the game.
   ```bash
   python connect4.py
   # or
   python3 connect4.py
   ```
---

### Deploying on Heroku

1. **Heroku Account:**
   - Make sure you have a Heroku account. If not, sign up on the Heroku website.
2. **GitHub Repository:**
   - Ensure your project is hosted on GitHub.
3. **Heroku Dashboard:**
   - Log in to your Heroku account and go to the Heroku Dashboard.
4. **Create a New App:**
   - On the dashboard, click `New` and choose `Create new app`.
5. **App Name:**
   - Choose a unique name for your app.
6. **Deployment Method:**
   - Click the `Deploy` tab.
   - In the `Deployment method` section, select "GitHub" as the deployment method.
7. **Authorize Heroku:**
   - Authorize Heroku to access your GitHub account.
8. **Search for Repository:**
   - Connect your GitHub repository to the Heroku app.
9. **Enable Automatic Deploys (Optional):**
   - Enable automatic deploys from a specific branch on GitHub.
10. **Manual Deploy (Optional):**
    - Manually deploy by clicking "Deploy Branch".
11. **View Deployment:**
    - Once deployed, view your live app by clicking "View".
---

### Essentials 
Things to remember when deploying Heroku App

- Code must be in the `run.py` file.
- Dependencies must be in the `requirements.txt` file.
- Do not edit other files, or your code may not deploy properly.
- When creating the app, add two buildpacks from the _Settings_ tab:
    1. `heroku/python`
    2. `heroku/nodejs`

- Create a _Config Var_ called `PORT` and set it to `8000`.
- If you have credentials, create another _Config Var_ called `CREDS` and paste the JSON into the value field.
- Connect your GitHub repository and deploy as normal.

### Constraints

The deployment terminal is set to 80 columns by 24 rows. Each line of text needs to be 80 characters or less; otherwise, it will be wrapped onto a second line.

---

## Testing
### Validator Testing with Flake8 and fixing

I used flake8 to test whether my code fits the pep8 standard. In terminal, I run
```bash
 flake8 run.py
 ```
 It returned a long list of errors including, `E501` for line too long.
 After analysing those lines, I found those line to be neccessarily long. Hence,
 ```bash
 flake8 --ignore=E50
1 run.py
```
This printed other errors that needed to be fixed.

After fixing my code, I tested to see if everything was working. 
Then I used pycodestyle (formerly known as pep8) to rerun the code. The error was fixed except for E501 errors.

`Running pycodestyle:

```bash
pycodestyle run.py
```


<details>
<summary> View errors from flake8</summary>

- run.py:6:1: F401 'random' imported but unused
- run.py:19:13: E225 missing whitespace around operator
- run.py:19:83: W291 trailing whitespace
- run.py:21:79: W291 trailing whitespace
- run.py:26:15: E225 missing whitespace around operator
- run.py:33:1: E302 expected 2 blank lines, found 1
- run.py:41:42: E231 missing whitespace after ','
- run.py:42:55: W291 trailing whitespace
- run.py:45:1: E302 expected 2 blank lines, found 1
- run.py:47:63: W291 trailing whitespace
- run.py:49:55: W291 trailing whitespace
- run.py:54:1: E302 expected 2 blank lines, found 1
- run.py:70:1: E302 expected 2 blank lines, found 1
- run.py:78:1: E302 expected 2 blank lines, found 1
- run.py:94:1: E302 expected 2 blank lines, found 1
- run.py:104:1: E302 expected 2 blank lines, found 1
- run.py:147:1: E302 expected 2 blank lines, found 1
- run.py:149:65: W291 trailing whitespace
- run.py:157:17: W503 line break before binary operator
- run.py:158:17: W503 line break before binary operator
- run.py:159:17: W503 line break before binary operator
- run.py:167:17: W503 line break before binary operator
- run.py:168:17: W503 line break before binary operator
- run.py:169:17: W503 line break before binary operator
- run.py:177:17: W503 line break before binary operator
- run.py:178:17: W503 line break before binary operator
- run.py:179:17: W503 line break before binary operator
- run.py:187:17: W503 line break before binary operator
- run.py:188:17: W503 line break before binary operator
- run.py:189:17: W503 line break before binary operator
- run.py:195:1: E302 expected 2 blank lines, found 1

</details>
<br>
<details>
<summary> Errors retrieved by pycodestyle </summary>

- run.py:19:80: E501 line too long (83 > 79 characters)
- run.py:20:80: E501 line too long (124 > 79 characters)
- run.py:22:80: E501 line too long (132 > 79 characters)
- run.py:24:80: E501 line too long (81 > 79 characters)
- run.py:26:80: E501 line too long (85 > 79 characters)
- run.py:27:80: E501 line too long (127 > 79 characters)
- run.py:29:80: E501 line too long (132 > 79 characters)
- run.py:30:80: E501 line too long (86 > 79 characters)
- run.py:31:80: E501 line too long (82 > 79 characters)
- run.py:36:80: E501 line too long (95 > 79 characters)
- run.py:77:80: E501 line too long (83 > 79 characters)
- run.py:78:80: E501 line too long (86 > 79 characters)
- run.py:136:80: E501 line too long (134 > 79 characters)
- run.py:139:80: E501 line too long (85 > 79 characters)
- run.py:141:80: E501 line too long (90 > 79 characters)
- run.py:145:80: E501 line too long (103 > 79 characters)
- run.py:215:80: E501 line too long (107 > 79 characters)
- run.py:276:80: E501 line too long (81 > 79 characters)
- run.py:355:80: E501 line too long (106 > 79 characters)
- run.py:450:80: E501 line too long (110 > 79 characters)
- run.py:457:80: E501 line too long (82 > 79 characters)
- run.py:499:80: E501 line too long (84 > 79 characters)
</details>

<br>

<details>
 <summary> Why E501 was ignored? </summary>
E501 error signifies that code exceeds the maximum line length specified under PEP8 (79 characters for code). I chose to ignore these errors because, the length of line was needed for readability and practicality such as code for creating the rules as a list.
</details>

---
<br>

# Acknowledgements 
- I would like to thank Gareth McGirr for the assistance in doing this project. Advice such as adding colorama.
- I would like to thank Kasia Bogucka of code institute for the advice and support.
***

 ### Website references
 <br>

 *Game logic and planning aid*
  - [How to code connect 4 in python](https://www.youtube.com/watch?v=i_4ZWjmybWs&ab_channel=ShaunHalverson)
- [Connect four in python](https://www.askpython.com/python/examples/connect-four-game)
   * This website was helpful and an inspiration for the game. It helped with understanding and knowing how to set up the game board.
- [Logic of connect 4](https://stackoverflow.com/questions/24400057/connect-4-game-logic)
- [Simple python connect 4](https://codereview.stackexchange.com/questions/225840/a-simple-connect-4-game-in-python)

*Minmaxing and AI logics in game development*
- [Artificial Intelligence at Play — Connect Four (Mini-max algorithm explained)](https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f)
- [Minmaxing in Tic-Tac-Toe](https://www.youtube.com/watch?v=trKjYdBASyQ&ab_channel=TheCodingTrain)
- [Kylie Ying- Tic tac toe](https://www.youtube.com/watch?v=fT3YWCKvuQE&ab_channel=KylieYing)
- [Minimax Algorithm in game theory](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)

*Additional features*
- [How to add time delay](https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/)
- [How to use pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)


## Future Features
- Implement pygame in this code
- Add varying levels of difficulty to computer play
- Responsive design so that it can work when deployed via cloud-based platform on different screen sizes.
- Social media integration and communication so that people can play on the same board on different computers.
