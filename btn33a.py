#
# File:      btn33a.py   "Read buttons on GPIO Pins for AF 4484"
#              (see  btn33b.py  for  AF 4506)
# Author:    David Johnson
#
# Description:
# This program allows the user to press a button and print a message.
#
# Sample Call:  python btn33a.py
#
# Modifications:
#  10/19/16   DCJ   Original version

from gpiozero import Button
from signal import pause
import time

curr_ms = lambda: int(round(time.time() * 1000))

global prev_off_ms
prev_off_ms = curr_ms()

global btn_start_ms
btn_start_ms = prev_off_ms


def start_button(btn):
    global btn_start_ms
    btn_start_ms = curr_ms()
    delta_sec = (btn_start_ms - prev_off_ms) * 0.001
    nas = str(btn.pin.number)
    text = NBR2LTR[nas]
    print(text+" button pressed (GPIO "+nas+"); no buttons for " + str(round(delta_sec,1)) + " sec.")

def stop_button():
    global prev_off_ms
    prev_off_ms = curr_ms()
    delta_sec = (prev_off_ms - btn_start_ms) * 0.001
    print("    pressed about " + str(round(delta_sec,1)) + " sec.\n")

NBR2LTR = {
    "23": "T",  #    COMMENT OUT  for  AF 4506;  activate for AF 4484
    "24": "B"   #    COMMENT OUT  for  AF 4506;  activate for AF 4484
}    

buttonT = Button(23)   #    COMMENT OUT  for  AF 4506;  activate for AF 4484
buttonB = Button(24)   #    COMMENT OUT  for  AF 4506;  activate for AF 4484

buttonT.when_pressed = start_button
buttonB.when_pressed = start_button

buttonT.when_released = stop_button
buttonB.when_released = stop_button

pause()
