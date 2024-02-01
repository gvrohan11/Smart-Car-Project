from gpiozero import Robot
from time import sleep

front_wheels = Robot(left=(23, 24), right=(16, 20))

# 23, 24 - left
# 16, 20 - right

'''

USING MECCANUM WHEELS

Left:

TL down, TR up
BL up, BR down

Right:

TL up, TR down
BL down, BR up

'''

def stop():
    front_wheels.stop()

def forward():
    front_wheels.forward()
    sleep(1)
    front_wheels.stop()

def backward():
    front_wheels.backward()
    sleep(1)
    front_wheels.stop()

def left():
    front_wheels.left()
    sleep(1)
    front_wheels.stop()

def right():
    front_wheels.right()
    sleep(1)
    front_wheels.stop()

def move_left_continuous():
    front_wheels.left()

def move_right_continuous():
    front_wheels.right()

def move_forward_continuous():
    front_wheels.forward()

def move_backward_continuous():
    front_wheels.backward()



