from abc import ABC, abstractmethod  


class I_Sender(ABC):
    @abstractmethod
    def sendMessage(self, message):
        pass

    @abstractmethod
    def sendPhoto(self, path):
        pass

    #Получатель
    @abstractmethod
    def setRecipient(self):
        pass