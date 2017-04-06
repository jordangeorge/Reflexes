from gpiozero import LED, Button
from time import sleep,time
import time
from random import randint, seed

red = LED(23)
green = LED(24)
blue = LED(25)

button = Button(26)
def run():
    count = 0

    print "Test Your Reflexes 1.0"
    name = raw_input("What is your name?")
    raw_input("Press any button when ready")
    
    seed()
    one = randint(0,9)
    seed()
    two = randint(0,9)
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
        mystring =  "Hello " + name + " Your score is " + str(format(yourtime, '.10f'))

        print mystring

        red.off()

        with open("scores.txt", "a") as myfile:
            myfile.write("Name: " + name + "---------------- Score: " + str(format(yourtime, '.10f')))
            break;

        
        
 

    
run()
    
