import I_sender as I


class Telegram(I.I_Sender):
    def sendMessage(self, message):
        print(message)

    def sendPhoto(self, path):
        pass

    def setRecipient(self):
        pass
