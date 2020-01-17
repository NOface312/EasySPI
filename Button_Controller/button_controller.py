import sys
from Sender_Controller.sender_controller import Sender_Controller
from Sender_Controller.Senders.console import Console
from Sender_Controller.Senders.vk import VK
from Sender_Controller.Senders.telegram import Telegram
from Sender_Controller.Senders.whatsapp import WhatsApp


class Button_Controller():
    def __init__(self):
        self.List_Senders = [WhatsApp(), VK(), Telegram(), Console()]
        self._sender_controller = Sender_Controller(Console())

    def Iteration(self):
        self._sender_controller.Iterator()

    def SendMessage(self):
        for sender in self.List_Senders:
            self._sender_controller._sender = sender
            if self._sender_controller.Send():
                break
        self._sender_controller.countOfPush = 0

    def MakePhoto(self):
        self._sender_controller.MakePhoto()
