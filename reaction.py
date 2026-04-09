from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
led.on()
# 随机延时5-10秒
sleep(uniform(5, 10))
led.off()
