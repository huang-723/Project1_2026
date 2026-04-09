from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
left_button = Button(14)
right_button = Button(15)

left_name = input("Left player name: ")
right_name = input("Right player name: ")

left_score = 0
right_score = 0

def pressed(button):
    global left_score, right_score
    if button.pin.number == 14:
        print(left_name + " won this round!")
        left_score += 1
    else:
        print(right_name + " won this round!")
        right_score += 1
    print("Total Score: " + left_name + ": " + str(left_score) + " | " + right_name + ": " + str(right_score))
    print("Next round will start soon...")


right_button.when_pressed = pressed
left_button.when_pressed = pressed

while True:
    print("\n=== New Round ===")
    led.on()
    sleep(uniform(5, 10))
    led.off()
    sleep(0.3)