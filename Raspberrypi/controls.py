from gpiozero import Robot
from time import sleep

front_wheels = Robot(left=(23, 24), right=(16, 20))
# back_wheels = Robot(left=(), right=())
back_wheels = Robot(left=(2, 3), right=(4, 17))
'''

FRONT WHEELS

23, 24 - left
16, 20 - right

BACK WHEELS

USING MECCANUM WHEELS

Left:

TL down, TR up
BL up, BR down

Right:

TL up, TR down
BL down, BR up

Turn Left:

TL down, TR up
BL down, BR up

Turn Right:

TL up, TR down
BL up, BR down

'''

def stop():
    front_wheels.stop()
    back_wheels.stop()

def forward():
    front_wheels.forward()
    back_wheels.forward()
    sleep(1)
    front_wheels.stop()
    back_wheels.stop()

def backward():
    front_wheels.backward()
    back_wheels.backward()
    sleep(1)
    front_wheels.stop()
    back_wheels.stop()

def left():
    front_wheels.left()
    back_wheels.right()
    sleep(1)
    front_wheels.stop()
    back_wheels.stop()

def right():
    front_wheels.right()
    back_wheels.left()
    sleep(1)
    front_wheels.stop()
    back_wheels.stop()

def move_left_continuous():
    front_wheels.left()
    back_wheels.right()

def move_right_continuous():
    front_wheels.right()
    back_wheels.left()

def move_forward_continuous():
    front_wheels.forward()
    back_wheels.forward()

def move_backward_continuous():
    front_wheels.backward()
    back_wheels.backward()

def turn_left():
    front_wheels.left()
    back_wheels.left()
    sleep(1)
    front_wheels.stop()
    back_wheels.stop()

def turn_right():
    front_wheels.right()
    back_wheels.right()
    sleep(1)
    front_wheels.stop()
    back_wheels.stop()

def turn_left_continuous():
    front_wheels.left()
    # back_wheels.left()

def turn_right_continuous():
    front_wheels.right()
    # back_wheels.right()



