# ACE Mini Quiz App

A simple command-line quiz application made using Python.

## Features

- Contains 10 multiple-choice questions
- Displays questions one at a time
- Keeps track of the score
- Shows the correct answer if the user is wrong
- Displays the final score and percentage
- Shows a performance message
- Questions are randomized

## Approach

The questions are stored in a list of dictionaries. Each dictionary
contains the question, its options and the correct answer.

I used separate functions for displaying questions, running the quiz
and showing the final result.

The score is increased whenever the user gives the correct answer.
The questions are shuffled using the random module so that they can
appear in a different order each time.

## Language

Python
