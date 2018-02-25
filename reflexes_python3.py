from gpiozero import LED, Button
from time import sleep, time
import time
from random import randint, seed
from operator import itemgetter

green = LED(25)
blue = LED(24)
red = LED(23)

button = Button(26)

def run():
    while(1):
        print("Test Your Reflexes 2.0")
        name = input("What is your name? ") # saves player's name in the 'name' variable
        input("Press ENTER on the keyboard when ready") # waits for player to press the enter key

        seed()
        one = randint(0, 9) # assigns random number to the 'one' variable
        seed()
        two = randint(0, 9) # assigns random number to the 'two' variable
        seed()

        green.on() # turn green LED on
        sleep(one) # keep light on for value saved in 'one'
        green.off() # turn green LED off

        blue.on()
        sleep(two)
        blue.off()

        red.on() # turn red LED on

        start = time.time() # start timer

        while True:
            button.wait_for_press() # wait for player to press button on breadboard
            finish = time.time() # end timer
            yourTime = finish - start # assigns time between red button turning on and player pressing button to 'yourTime'
            scoreStr =  "Hello, " + name + ". Your score is " + str(format(yourTime, '.5f') + "!")

            print(scoreStr) # shows player their time/score

            red.off() # turn red LED off

            with open("scores.txt", "a") as scoresFile: # open scores.txt; if there is no scores.txt file, create one
                entry = ("Name: " + name + "\t Score: " + str(format(yourTime, '.5f')) + "\n").expandtabs(30)
                scoresFile.write(entry) # save score to file
                break; # end while loop                

        print('\n')

run()
