from camera import makePhotos


class Sender_Controller():
    def __init__(self, sender):

        self.countOfPush = 0
        self.messageArray = ["Null","Yes", "No", "Repeat!", "Can't speak", "Photo!"]
        self._sender = sender

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    def Iterator(self):
        self.countOfPush += 1
    
    def MakePhoto(self):
        return makePhotos(5)

    def Send(self):
        try:
            if self.countOfPush <= len(self.messageArray):
                self._sender.sendMessage(self.messageArray[self.countOfPush])
                if self.countOfPush == 5:
                    self._sender.sendPhoto(self.MakePhoto())
            else:
                print("Button has pushed x" + str(self.countOfPush))
        except:
            return False
        
        return True