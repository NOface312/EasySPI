import time
import picamera
from pynput.mouse import Listener

import buttons as bt

left_mouse_button = None
right_mouse_button = None
midle_mouse_button = None

button_controller = bt.Buttons()

def on_click(x, y, button, pressed):
    if pressed:
        if str(button) == "Button.left":
            button_controller.sendMessage()
        if str(button) == "Button.right":
            button_controller.Iterator()

with Listener(on_click = on_click) as listener:
    listener.join()



