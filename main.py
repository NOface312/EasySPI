import sys
import os
sys.path.append("Button_Controller")
sys.path.append("Button_Controller/Sender_Controller")
sys.path.append("Button_Controller/Sender_Controller/Senders")

from Button_Controller.button_controller import Button_Controller
import time
from pynput.mouse import Listener


global button_controller 
button_controller = Button_Controller()

def on_click(x, y, button, pressed):
    global button_controller
    if pressed:
        if str(button) == "Button.left":
            button_controller.SendMessage()
        if str(button) == "Button.right":
            button_controller.Iteration()
        if str(button) == "Button.middle":
            button_controller.MakePhoto()



if __name__ == "__main__":
    with Listener(on_click = on_click) as listener:
        listener.join()