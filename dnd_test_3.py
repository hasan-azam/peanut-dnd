# This example shows you a simple, non-interrupt way of reading Pico Display's buttons with a loop that checks to see if buttons are pressed.
# https://www.raspberrypi.com/news/graphic-routines-for-raspberry-pi-pico-screens/
# Use this for help with the functions!

import time
import random
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_P4, PEN_RGB332
import jpegdec
from pimoroni import RGBLED



# We're only using a few colours so we can use a 4 bit/16 colour palette and save RAM!
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB332, rotate=0)

display.set_backlight(1.0)
display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)


WIDTH, HEIGHT = display.get_bounds()


WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)


led = RGBLED(6, 7, 8)




# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()


# set up

    #display.set_pen(GREEN)
    #display.set_font("gothic")
    #display.text("Welcome to P.E.A.N.U.T.", 70, 70, 240, 0.5)
    #display.update()
    #time.sleep(5)
clear()


display.set_font("bitmap8")

def statsMenu():
    clear()
    display.set_font("bitmap8")
    while True:
        if button_a.read():                                   # if a button press is detected then...
            clear()                                           # clear to black
            display.set_pen(GREEN)
            # change the pen colour
            
            display.text("Force Empowered Rend!", 65, 25, 1000, 2.5)  # display some text on the screen
            
            #display.rectangle(100, 50 ,25 ,25)
            #display.rectangle(100, 20 ,50 ,50) 
            display.set_pen(BLACK)
            #display.rectangle(110, 25 ,25 ,25)
            display.set_pen(MAGENTA)
            display.text("Attack: +4 to hit, reach 5 ft., one target you can see. Hit: 1d8 + 2 force damage.", 30, 70, 250, 2)
            
            toHit = random.randint(0,20)
            damage = random.randint(0,8)
            
            display.text(f"Hit: {toHit} +4 = {toHit+4}", 30, 150, 250, 2)
            display.text(f"Damage: {damage} +2 = {damage+2} force damage", 30, 175, 1000, 2)


            

    #Draws a filled rectangle from point(x, y), w pixels wide and h pixels high.

            # display.text("Text", X-Pos, Y-Pos, text wrapping, size)
            
            display.update()                                  # update the display
            time.sleep(10)                                     # pause for a sec
            clear()                                           # clear to black again
        elif button_b.read():
            clear()                                           # clear to black
            display.set_pen(GREEN)                            # change the pen colour
            display.text("Repair (3/Day)!", 70, 25, 1000, 2.5)  # display some text on the screen
            
            display.set_pen(BLACK)
            display.set_pen(MAGENTA)
            display.text("The magical mechanisms inside the defender restore 2d8 + 2 hit points to itself or to one construct or object within 5 feet of it",  30, 70, 250, 2)
            
            healAmount = random.randint(1,8) + random.randint(1,8)
            
            display.text(f"Heal: {healAmount} + 2 = {healAmount+2} ", 30, 175, 1000, 2)

            display.update()
            time.sleep(10)
            clear()
        elif button_x.read():
            clear()
            #display.set_pen(MAGENTA)
            #display.text("Button X pressed", 10, 10, 240, 4)
            #display.update()
            #time.sleep(1)
            statsMenu()
            #clear()
        elif button_y.read():
            clear()
            actionMenu()
        else:
        
            
            display.set_pen(GREEN)
            display.text("HP:", 15, 57, 10, 2)
            display.text("Peanut's Stats!", 215, 57, 10, 2)

            display.text("Back!", 230, 175, 10, 2)
            display.set_font("gothic")
            display.text("Stats Menu!", 50, 25, 240, 1)
            display.set_font("bitmap8")







            display.update()

        time.sleep(0.1)  # this number is how frequently the Pico checks for button presses



def actionMenu():
    clear()
    display.set_font("bitmap8")
    while True:
        if button_a.read():                                   # if a button press is detected then...
            clear()                                           # clear to black
            display.set_pen(GREEN)
            # change the pen colour
            
            display.text("Force Empowered Rend!", 65, 25, 1000, 2.5)  # display some text on the screen
            
            #display.rectangle(100, 50 ,25 ,25)
            #display.rectangle(100, 20 ,50 ,50) 
            display.set_pen(BLACK)
            #display.rectangle(110, 25 ,25 ,25)
            display.set_pen(MAGENTA)
            display.text("Attack: +4 to hit, reach 5 ft., one target you can see. Hit: 1d8 + 2 force damage.", 30, 70, 250, 2)
            
            toHit = random.randint(0,20)
            damage = random.randint(0,8)
            
            display.text(f"Hit: {toHit} +4 = {toHit+4}", 30, 150, 250, 2)
            display.text(f"Damage: {damage} +2 = {damage+2} force damage", 30, 175, 1000, 2)


            

    #Draws a filled rectangle from point(x, y), w pixels wide and h pixels high.

            # display.text("Text", X-Pos, Y-Pos, text wrapping, size)
            
            display.update()                                  # update the display
            time.sleep(10)                                     # pause for a sec
            clear()                                           # clear to black again
        elif button_b.read():
            clear()                                           # clear to black
            display.set_pen(GREEN)                            # change the pen colour
            display.text("Repair (3/Day)!", 70, 25, 1000, 2.5)  # display some text on the screen
            
            display.set_pen(BLACK)
            display.set_pen(MAGENTA)
            display.text("The magical mechanisms inside the defender restore 2d8 + 2 hit points to itself or to one construct or object within 5 feet of it",  30, 70, 250, 2)
            
            healAmount = random.randint(1,8) + random.randint(1,8)
            
            display.text(f"Heal: {healAmount} + 2 = {healAmount+2} ", 30, 175, 1000, 2)

            display.update()
            time.sleep(10)
            clear()
        elif button_x.read():
            clear()
            #display.set_pen(MAGENTA)
            #display.text("Button X pressed", 10, 10, 240, 4)
            #display.update()
            #time.sleep(1)
            statsMenu()
            #clear()
        elif button_y.read():
            clear()
            display.set_pen(YELLOW)
            display.text("Button Y pressed", 10, 10, 240, 4)
            display.update()
            time.sleep(1)
            clear()
        else:
        
            
            display.set_pen(GREEN)
            display.text("Force Empowered Rend!", 15, 57, 10, 2)
            display.text("Peanut's Stats!", 215, 57, 10, 2)

            display.text("Repair (3/Day)!", 15, 175, 10, 2)
            display.set_font("gothic")
            display.text("Pick an Action!", 50, 25, 240, 1)
            display.set_font("bitmap8")







            display.update()

        time.sleep(0.1)  # this number is how frequently the Pico checks for button presses


def bootMessage():
    display.set_pen(GREEN)
    display.set_font("gothic")
    display.text("P.E.A.N.U.T.", 35, 75, 240, 1.3)
    display.set_font("bitmap8")
    #display.text("Pneumatic Electronic Animal Networked to Understand Thelmor", 32, 75, 250, 2)
    display.text("Pneumatic Electronic Animal", 33, 110, 250, 2)
    display.text("Networked to Understand", 47, 135, 250, 2)
    display.text("Thelmor", 125, 160, 250, 2)

    display.update()
    led.set_rgb(255, 0, 0)
    time.sleep(1)
    led.set_rgb(255, 255, 0)
    time.sleep(1)
    led.set_rgb(0, 255, 0)

    
    
    time.sleep(3)
    led.set_rgb(0, 0, 0)
    

#Done with definitions, now let's do stuff!
    
bootMessage()
actionMenu()
