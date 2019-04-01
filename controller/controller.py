from pygame import joystick
import pygame
import time
import serial
import struct

pygame.display.init()
joystick.init()
j = joystick.Joystick(0)
j.init()

s = serial.Serial("/dev/ttyACM0")


def tf(x): return x*x*x*abs(x)


while True:
    pygame.event.pump()

    # transform the stick inputs
    lh = tf(j.get_axis(0))
    lv = tf(j.get_axis(1))
    rh = tf(j.get_axis(3))
    rv = tf(j.get_axis(4))

    # transform between sticks and the coils
    north_c = max(0.0, -lv) + min(0.0, rv)
    south_c = max(0.0, lv) + min(0.0, -rv)
    west_c = max(0.0, -lh) + min(0.0, rh)
    east_c = max(0.0, lh) + min(0.0, -rh)
    s.write(struct.pack("ffff", north_c, east_c, west_c, south_c))
    print(("north: {: .4f} south: {: .4f}"
          + " east: {: .4f} west: {: .4f}").format(north_c, south_c,
                                                  east_c, west_c),
          end="\r")
    time.sleep(.05)
