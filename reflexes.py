from gpiozero import LED, Button
from time import sleep, time
import time
from random import randint, seed

green = LED(25)
blue = LED(24)
red = LED(23)

button = Button(26)

def run():
    print "Test Your Reflexes 1.0"
    name = raw_input("What is your name? ")
    raw_input("Press ENTER on the keyboard when ready")

    seed()
    one = randint(0, 9)
    seed()
    two = randint(0, 9)
    seed()

    green.on()
    sleep(one)
    green.off()

    blue.on()
    sleep(two)
    blue.off()

    red.on()

    start = time.time()

    while True:
        button.wait_for_press()
        finish = time.time()
        yourtime = finish - start
        mystring =  "Hello, " + name + ". Your score is " + str(format(yourtime, '.5f'))

        print mystring

        red.off()

        with open("scores.txt", "a") as scoresFile:
            entry = ("Name: " + name + "\t Score: " + str(format(yourtime, '.5f')) + "\n").expandtabs(30)
            scoresFile.write(entry)
            break;

run()
