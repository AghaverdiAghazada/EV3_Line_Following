#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=120)

DRIVE_SPEED = 100
TURN_RATE = 100
TARGET_COLOR = Color.GREEN

current_position = "straight"
gray_line_count = 0

def gray_color(color_value):
    return color_value not in [
        Color.BLACK,
        Color.WHITE,
        Color.RED,
        Color.BLUE,
        Color.GREEN,
        Color.YELLOW,
        Color.BROWN,
        None
    ]

while True:
    left_color = left_sensor.color()
    right_color = right_sensor.color()

    if gray_color(left_color) or gray_color(right_color):
        if gray_line_count == 0:

            robot.stop()
            ev3.speaker.beep()
            wait(100)
            robot.turn(360)   
            wait(100)
            gray_line_count += 1
            continue

        elif gray_line_count == 1:
            robot.stop()
            ev3.speaker.beep()
            ev3.screen.print("Stopped at the second gray line.")
            break

    if left_color == TARGET_COLOR and right_color != TARGET_COLOR:
        robot.drive(DRIVE_SPEED, -TURN_RATE)
        current_position = "left"

    elif right_color == TARGET_COLOR and left_color != TARGET_COLOR:
        robot.drive(DRIVE_SPEED, TURN_RATE)
        current_position = "right"

    elif left_color == TARGET_COLOR and right_color == TARGET_COLOR:
        if current_position == "left":
            robot.drive(DRIVE_SPEED, -TURN_RATE)
        else:
            if current_position == "left":
                robot.drive(DRIVE_SPEED, -TURN_RATE)
            elif current_posiiton == "right":
                robot.drive(DRIVE_SPEED, TURN_RATE)
        current_position = "straight"

    else:

        robot.drive(DRIVE_SPEED, 0)

    wait(10)