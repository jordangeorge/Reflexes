# [Reflexes](https://github.com/jordangeorge/Reflexes)

## Contents
- Images folder
  - Helpful images for creating the project
  - Raspberry pi 3 gpio pinout image - helpful for creating the project
- rank and average scores.ipynb
  - Jupyter notebook that ranks and filters scores from the scores.txt file and stores them in ranked-filtered-scores.xlsx
  - Also averages the scores
- ranked-filtered-scores.xlsx
  - Excel file containing ranked and filtered scores in ascending order
- ranked-scores.txt
  - Ranked scores in ascending order
- reflexes.py
  - Python 2 version
- reflexes_python3.py
  - Python 3 version
- scores.txt
  - All scores saved and shown here

## About

Test your reflexes in this exciting Raspberry Pi game designed with the intention of teaching kids about computer science and engineering. Made for Engineers Day (E-Day) 2017 at the University of Kentucky. This project has been featured at E-Day 2017-2019 as well as the Gatton Student Center Spectacular in 2018.

Once the program is run, the player enters their name and presses the 'enter' key twice to start the game. The player must then wait for the third/red LED to light up to press the button as quick as they can.

The average score is approximately 0.23. Getting less than 0.2 means that the player has great reflexes! Scores that are around 0.00006 are 'cheaters' because they're most likely holding the button down. Scores above 0.4 are typically a result of people becoming acclimated to the game, younger players, and various other reasons. Therefore, these were filtered out of the average.

Program was originally created using the Raspberry Pi 3 Model B and Python 2.

## Setup

###### Step 1
[Get started with your Raspberry Pi using this link](https://www.imore.com/how-get-started-using-raspberry-pi).

###### Step 2
Once you've completed getting started with the Raspberry Pi, you can set up the physical aspect of this project.

What you'll need:
- A breadboard
- 5 Male-to-Female jumper/DuPont wires
- 4 Female-to-Female jumper/DuPont wires
- 4 resistors
- 3 LED lights, preferably all being different colors or one being a different color from the other two
- Button

###### Step 3
Setup everything like in the pictures below.

###### Step 4
Either
* download the repository within Raspbian

or

* download it onto a flash drive and connect that to your Raspberry Pi and copy the file to your Raspbian desktop or any other directory.

###### Step 5
Open `reflexes_python3.py` and run it. This can be done within the terminal or a python compatible IDE.

###### Step 6 (optional)
Use `watch -n 1 tail scores.txt` in the terminal to see live additions to the scores.txt file.

## Helpful Images
![](images/pi3-gpio-pinout.png)
![](images/IMG_1978.jpg)
![](images/IMG_1979.jpg)
![](images/IMG_1980.jpg)
![](images/IMG_1981.jpg)
![](images/IMG_1982.jpg)
![](images/IMG_1983.jpg)
