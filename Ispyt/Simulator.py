import random
from CategoriesOfTransport import Bus, Tram, Trolleybus
from Tram_schedule import TransportInformation


class Route:
    def __init__(self, name, stops):
        self.name = name
        self.stops = stops

    def showRoute(self):
        print(f"Маршрут: {self.name}")
        for index, stop in enumerate(self.stops):
            print(f"{index + 1}. {stop}")


class ScheduleBus(Bus):
    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime, transport, route, interval_between_stops):
        self.transport = transport
        self.route = route
        self.interval_between_stops = interval_between_stops
        self.current_time = 8 * 60  # Початковий час 8:00
        self.end_time = 22 * 60  # Кінцевий час 22:00
        super().__init__(model, speed, pathLength, numberOfStops, arrivalTime)

    def showTime(self):
        bus.time()

    def convert_minutes_to_time(self, total_minutes):
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02d}:{minutes:02d}"

    def simulate(self):
        print(f"Симуляція маршруту {self.route.name} для {self.transport.model} (Швидкість: {self.transport.speed} км/год)")

        while self.current_time < self.end_time:
            for stop in self.route.stops:
                if self.current_time >= self.end_time:
                    break

                delay = random.randint(-3, 3)  # Генеруємо затримку або випередження в хвилинах
                self.current_time += self.interval_between_stops + delay

                formatted_time = self.convert_minutes_to_time(self.current_time)
                if delay == 0:
                    status = "на часі"
                elif delay > 0:
                    status = f'запізнення на {delay} хв'
                else:
                    status = f'випередження на {delay *(-1)} хв'
                print(f"Прибуття на зупинку {stop}: {formatted_time} ({status})")


class ScheduleTroll(Trolleybus):
    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime, transport, route, interval_between_stops):
        self.transport = transport
        self.route = route
        self.interval_between_stops = interval_between_stops
        self.current_time = 8 * 60  # Початковий час 8:00
        self.end_time = 22 * 60  # Кінцевий час 22:00
        super().__init__(model, speed, pathLength, numberOfStops, arrivalTime)

    def showTime(self):
        trolleybus.time()

    def convert_minutes_to_time(self, total_minutes):
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02d}:{minutes:02d}"

    def simulate(self):
        print(f"Симуляція маршруту {self.route.name} для {self.transport.model} (Швидкість: {self.transport.speed} км/год)")

        while self.current_time < self.end_time:
            for stop in self.route.stops:
                if self.current_time >= self.end_time:
                    break

                delay = random.randint(-3, 3)  # Генеруємо затримку або випередження в хвилинах
                self.current_time += self.interval_between_stops + delay

                formatted_time = self.convert_minutes_to_time(self.current_time)
                if delay == 0:
                    status = "на часі"
                elif delay > 0:
                    status = 'запізнення'
                else:
                    status = 'випередження'
                print(f"Прибуття на зупинку {stop}: {formatted_time} ({status})")


class ScheduleTram(Tram):
    def __init__(self, model, speed, pathLength, numberOfStops, arrivalTime, transport, route, interval_between_stops):
        self.transport = transport
        self.route = route
        self.interval_between_stops = interval_between_stops
        self.current_time = 8 * 60  # Початковий час 8:00
        self.end_time = 22 * 60  # Кінцевий час 22:00
        super().__init__(model, speed, pathLength, numberOfStops, arrivalTime)

    def showTime(self):
        tram.time()

    def convert_minutes_to_time(self, total_minutes):
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"{hours:02d}:{minutes:02d}"

    def simulate(self):
        print(f"Симуляція маршруту {self.route.name} для {self.transport.model} (Швидкість: {self.transport.speed} км/год)")

        while self.current_time < self.end_time:
            for stop in self.route.stops:
                if self.current_time >= self.end_time:
                    break

                delay = random.randint(-3, 3)  # Генеруємо затримку або випередження в хвилинах
                self.current_time += self.interval_between_stops + delay

                formatted_time = self.convert_minutes_to_time(self.current_time)
                if delay == 0:
                    status = "на часі"
                elif delay > 0:
                    status = 'запізнення'
                else:
                    status = 'випередження'
                print(f"Прибуття на зупинку {stop}: {formatted_time} ({status})")


# # Отримуємо маршрути з файлу Tram_schedule
# bus_info = TransportInformation('Автобус')
# tram_info = TransportInformation('Трамвай')
# trolleybus_info = TransportInformation('Тролейбус')
#
# # Створюємо маршрути на основі інформації з Tram_schedule
# bus_route = Route("Автобусний маршрут", bus_info.list_of_stops_bus_and_trolleybus)
# tram_route = Route("Трамвайний маршрут", tram_info.list_of_stops_tram)
#
# # Використовуємо транспортні засоби з файлу CategoriesOfTransport
# bus = Bus('Nissan', 30, 600, 10, 0)  # Додано arrivalTime = 0
# tram = Tram('Tram', 40, 600, 10, 0)  # Додано arrivalTime = 0
# trolleybus = Trolleybus('Ford', 20, 600, 10, 0)  # Додано arrivalTime = 0
#
# # Встановлюємо розклад (інтервал між зупинками в хвилинах)
# bus_schedule = ScheduleBus('Bus', 30, 600, 10, 0, bus, bus_route, 5)  # Додано arrivalTime = 0
# tram_schedule = ScheduleTram('tram', 40, 600, 10, 0, tram, tram_route, 5)  # Додано arrivalTime = 0
# trolleybus_schedule = ScheduleTroll('trolleybus', 20, 600, 10, 0, trolleybus, bus_route, 5)  # Додано arrivalTime = 0
#
# bus.time()
# bus.showInfoBus()
#
# trolleybus.time()
# trolleybus.showInfoTrolleybus()
#
# tram.time()
# tram.showInfoTram()
#
# bus_info = TransportInformation('bus')
# bus_info.add_stop(1, 'lkdvfskjvdfkjvd', 9)
#
# # Симуляція руху
# print("\n=== Симуляція для автобуса ===")
# bus_schedule.simulate()
#
# print("\n=== Симуляція для трамвая ===")
# tram_schedule.simulate()
#
# print("\n=== Симуляція для тролейбуса ===")
# trolleybus_schedule.simulate()
#
#
#