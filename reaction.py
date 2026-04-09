from gpiozero import LED, Button
from time import sleep
from random import uniform

# 硬件初始化
led = LED(4)
left_button = Button(14)
right_button = Button(15)

# 输入玩家姓名
left_name = input('left player name is: ')
right_name = input('right player name is: ')

# 灯光逻辑
led.on()
sleep(uniform(5, 10))
led.off()

# 获胜判断
def pressed(button):
    if button.pin.number == 14:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
    # 结束程序
    exit()

# 绑定事件
right_button.when_pressed = pressed
left_button.when_pressed = pressed
