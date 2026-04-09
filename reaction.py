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
total_rounds = 3

def pressed(button):
    global left_score, right_score
    if button.pin.number == 14:
        print(left_name + " won this round!")
        left_score += 1
    else:
        print(right_name + " won this round!")
        right_score += 1
    print("Total Score: " + left_name + ": " + str(left_score) + " | " + right_name + ": " + str(right_score))

right_button.when_pressed = pressed
left_button.when_pressed = pressed

for round_num in range(1, total_rounds + 1):
    print("\n=== Round " + str(round_num) + " ===")
    led.on()
    sleep(uniform(5, 10))
    led.off()
    sleep(3)

print("\n=== Final Result ===")
print(left_name + ": " + str(left_score))
print(right_name + ": " + str(right_score))
if left_score > right_score:
    print(left_name + " is the winner!")
elif right_score > left_score:
    print(right_name + " is the winner!")
else:
    print("It's a tie!")
