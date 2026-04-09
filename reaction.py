from gpiozero import LED, Button
from time import sleep

# 初始化LED
led = LED(4)
# 点亮5秒后熄灭
led.on()
sleep(5)
led.off()
