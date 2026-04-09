from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input("Left player name: ")
right_name = input("Right player name: ")

def pressed(button):
    if button.pin.number == 14:
        print(left_name + " won the game!")
    else:
        print(right_name + " won the game!")
    print("Next round will start soon...")

right_button.when_pressed = pressed
left_button.when_pressed = pressed

while True:
    led.on()
    sleep(uniform(5, 10))
    led.off()
    sleep(0.3)
