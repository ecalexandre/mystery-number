## mystery-number 🔢🎲

## About it

This program is basically a game where you have to guess the number between a number and another number. For each attempts, there is going to be hints so you can win easily.

## Features

- User can type their name first to start the game.
- User can type a number to keep guessing the right number.

## Requirements

- Python 3.13 or Python 3.14

## Installation

1. Clone the repository with `git clone` command on the repository.
2. Create a virtual environment for your script with `python3 -m venv` command.
3. Activate the virtual environment with `source .venv/bin/activate` command

## Usage

>  Run your program by simply typing `python3 mystery-number.py` on the command line.

This should should appear when you start the program:

```
Enter your name to start the game (Press enter to finish): (name)
```

> So you would have to type your name
> When you're finished, this should show up after:

```
*************************************************************************************************************
Hello (name)! Welcome to the Guess The Number challenge! The game is about picking a number between 1 to 1000.
The game will continue as long as you did not get the right number!
If you get the right number, you will win and receive the amount of tries it took you to win!
So here are the rules:
1. Do not put a character that is not a number because you will never get the right answer by doing it.
2. If you ever put a number that is too high or too low, I am gonna give you hints to win easily.
Good luck!
*************************************************************************************************************
Enter your number here (Press enter to finish):
```

>  Here are the instructions for you. You have to guess the right number which is between 1 to 1000.
> You have to type a number

## Example

> If the right number is 156 and you type:

```
Enter your number here (Press enter to finish): 30
```

> Here is what it is going to tell you this: "Hint : Pssss, the correct number is above that"

## Project structure

```
mystery-number/
|__ mystery-number.py
|__ README.md
```

## Author

```
created by ecalexandre
```
