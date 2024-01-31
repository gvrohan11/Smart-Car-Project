import gpiozero as Robot
from time import sleep


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

front_wheels = Robot(left=(23, 24), right=(16, 20))

def robotForward():
    # front_wheels.left.forward()
    # front_wheels.right.forward()
    front_wheels.forward()

def robotBackward():
    # front_wheels.left.backward()
    # front_wheels.right.backward()
    front_wheels.backward()

def robotLeft():
    # front_wheels.left.backward()
    # front_wheels.right.forward()
    front_wheels.left()

def robotRight():
    # front_wheels.left.forward()
    # front_wheels.right.backward()
    front_wheels.right()

def stop():
    front_wheels.stop()