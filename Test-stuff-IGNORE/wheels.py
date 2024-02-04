from gpiozero import Robot
from time import sleep

front = Robot(left=(23, 24), right=(16, 20))
back = Robot(left=(2, 3), right=(4, 17))


for i in range(1):
    front.forward()
    back.forward()
    sleep(1)
    front.right()
    back.right()
    sleep(1)
    front.backward()
    back.backward()
    sleep(1)
    front.left()
    back.left()
    sleep(1)
    front.stop()
    back.stop()
    sleep(1)