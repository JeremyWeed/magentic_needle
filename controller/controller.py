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
    lh = tf(j.get_axis(0))
    lv = tf(j.get_axis(1))
    rh = tf(j.get_axis(3))
    rv = tf(j.get_axis(4))
    s.write(struct.pack("ffff", lh, lv, rh, rv))
    print("lh: {: .4f} lv: {: .4f} rh: {: .4f} rv: {: .4f}".format(lh, lv,
                                                                   rh, rv),
          end="\r")
    time.sleep(.05)
