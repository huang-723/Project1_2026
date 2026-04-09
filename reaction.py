from gpiozero import LED, Button
from time import sleep
from random import uniform

# 硬件初始化
led = LED(4)
left_button = Button(14)
right_button = Button(15)

# 灯光逻辑
led.on()
sleep(uniform(5, 10))
led.off()

# 按钮按压函数
def pressed(button):
    print(str(button.pin.number) + ' won the game')

# 绑定按压事件
right_button.when_pressed = pressed
left_button.when_pressed = pressed
