#
# File:      btn33b.py   "Read buttons on GPIO Pins for AF 4506"
#              (see  btn33a.py  for  AF 4484)
# Author:    David Johnson
#
# Description:
# This program allows the user to press a button and print a message.
#
# Sample Call:  python btn33b.py
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
    "17": "U",
    "22": "D",
    "27": "L",
    "23": "R",   # comment out for  AF 4484;   ACTIVATE  for  AF 4506
    "4": "C",
    "6": "T",    # comment out for  AF 4484;   ACTIVATE  for  AF 4506
    "5": "B"     # comment out for  AF 4484;   ACTIVATE  for  AF 4506
}    
    
buttonU = Button(17)
buttonD = Button(22)
buttonL = Button(27)
buttonR = Button(23)  # comment out for  AF 4484;   ACTIVATE  for  AF 4506
buttonC = Button(4)
buttonT = Button(6)   # comment out for  AF 4484;   ACTIVATE  for  AF 4506
buttonB = Button(5)   # comment out for  AF 4484;   ACTIVATE  for  AF 4506

buttonU.when_pressed = start_button
buttonD.when_pressed = start_button
buttonL.when_pressed = start_button
buttonR.when_pressed = start_button
buttonC.when_pressed = start_button
buttonT.when_pressed = start_button
buttonB.when_pressed = start_button

buttonU.when_released = stop_button
buttonD.when_released = stop_button
buttonL.when_released = stop_button
buttonR.when_released = stop_button
buttonC.when_released = stop_button
buttonT.when_released = stop_button
buttonB.when_released = stop_button

pause()
