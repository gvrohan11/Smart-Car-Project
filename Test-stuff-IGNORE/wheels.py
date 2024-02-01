from gpiozero import Robot
from time import sleep

robot = Robot(left=(23, 24), right=(16, 20))

while True:
    robot.forward()
    sleep(1)
    robot.right()
    sleep(1)
    robot.backward()
    sleep(1)
    robot.left()
    sleep(1)
    robot.stop()
    sleep(1)