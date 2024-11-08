from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    @abstractmethod
    def time(self):
        pass

    def showInfo(self):
        print(self.model, self.speed)