import camera as cm


class Buttons:
    def __init__(self):
        self.countOfPush = 0
        self.messageArray = ["Null","Yes", "No", "Repeat!", "Can't speak", "Photo!"]
          
    def sendMessage(self):
        if self.countOfPush <= len(self.messageArray):
            print(self.messageArray[self.countOfPush])
            if self.countOfPush == 5:
                print("Make photo in directory ..." + cm.makePhotos(4))
        else:
            print("Button has pushed x" + str(self.countOfPush))
        
        self.countOfPush = 0
    def Iterator(self):
        self.countOfPush += 1
    
    def sendPhoto(self):
        print("Make photo in directory ..." + cm.makePhotos(4))


        
