from TransportFile import Transport
import random

class Bus(Transport):
    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength # Відстань між зупинками
        self.numberOfStops = numberOfStops # Номер зупинки
        self.arrivalTime = arrivalTime # Загальний час від першої до тої зупинки який номер ввели

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / (self.speed * 3.6) # Розрахунок загального часу в секундах

        ran = random.randint(0,1) # Змінна для розрахунку запізнення або прискорення
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5) # Добавляє рандомне число
            self.arrivalTime /= 60 # Переводе секунди в хвилини
            self.arrivalTime += (3 * self.numberOfStops) # Добавляє час на зупинку
        else:
            self.arrivalTime -= random.randint(0,5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)

        return self.arrivalTime

    def showInfoBus(self):
        print(f'Автобус моделі: {self.model}, швидкість: {self.speed}, загальний час на маршрут: {self.arrivalTime}')

class Trolleybus(Transport):

    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / (self.speed * 3.6)

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)
        else:
            self.arrivalTime -= random.randint(0,5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)

        return self.arrivalTime

    def showInfoTrolleybus(self):
        print(f'Тролейбус моделі: {self.model}, швидкість: {self.speed}, Загальний час на маршрут: {self.arrivalTime}')
class Tram(Transport):

    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime = 0):
        super().__init__(model, speed)
        self.pathLength = pathLength
        self.numberOfStops = numberOfStops
        self.arrivalTime = arrivalTime

    def time(self):

        self.arrivalTime = (self.pathLength * self.numberOfStops) / (self.speed * 3.6)

        ran = random.randint(0,1)
        if ran == 0 :
            self.arrivalTime += random.randint(0, 5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)
        else:
            self.arrivalTime -= random.randint(0,5)
            self.arrivalTime /= 60
            self.arrivalTime += (3 * self.numberOfStops)

        return self.arrivalTime

    def showInfoTram(self):
        print(f'Трамвай моделі: {self.model}, швидкість: {self.speed}, загальний час на маршрут: {self.arrivalTime}')