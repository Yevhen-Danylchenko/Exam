class TransportInformation:
    def __init__(self, for_transport):
        self.for_transport = for_transport
        self.list_of_stops_bus_and_trolleybus = ["Паркова алея", 'Площа Незалежності', 'Залізничний вокзал',
                                                 'Бібліотека імені Шевченка', 'Вулиця Лесі Українки',
                                                 'Торговий центр "Глобус"', 'Палац спорту', "Міський парк",
                                                 'Кафедральний собор',
                                                 "Автобусний вокзал"]  # початковий список зупинок для автобуса та тролейбуса
        self.list_of_stops_tram = ["Ринкова площа", 'Парковий комплекс "Сосновий бір"', 'Ботанічний сад',
                                   'Торговий центр "Магелан"', 'Міська поліклініка', 'Кінотеатр "Україна"',
                                   'Вулиця Івана Франка', 'Площа Перемоги', 'Музей історії',
                                   "Спортивний комплекс 'Арена'"]  # початковий список зупинок для трамвая
        self.all_routes=[]
        self.all_routes.append(self.list_of_stops_tram)
        self.all_routes.append(self.list_of_stops_bus_and_trolleybus)

    def add_route(self, number_of_stops, for_transport):
        self.number_of_stops=number_of_stops
        self.for_transport=for_transport
        new_route =[]
        for i in range(number_of_stops):
            new_route.append(input(f"Введіть назву зупинки №{i+1}: "))
        self.all_routes.append(new_route)
        print(f"Новий маршрут для транспорту {self.for_transport} успішно додано!")
        first_stop=new_route[0]
        last_stop=new_route[-1]


    def delete_route(self, route_num_to_delete):
        if route_num_to_delete > 0 and route_num_to_delete<=len(self.all_routes):
            self.all_routes.pop(route_num_to_delete)
            print(f"Маршрут №{route_num_to_delete} для транспорту {self.for_transport} видалено")
        else:
            print("Маршруту з таким номером не існує")


    def show_route(self, route_num): #Виводить маршрут за його назвою

        if route_num > 0 and route_num<= len(self.all_routes):
            print(f"Маршрут №{route_num} для транспорту {self.for_transport}:")
            for index, i in enumerate(self.all_routes[route_num-1]):
                print(f"{index + 1} - {i}")
        else:
            print("Маршруту з таким номером не існує")

    def show_all_routes(self):
        for index, i in enumerate(self.all_routes):
            print(f"Маршрут № {index+1} для транспорту {self.for_transport}:")
            for index2, j in enumerate(i):
                print(f"{index2+1} - {j}")

    def add_stop(self, user_choice_route, new_stop_name, where_add_stop):
        self.user_choice_route=user_choice_route #номер маршруту
        self.new_stop_name=new_stop_name #назву зупинки
        self.where_add_stop=where_add_stop # На яке місце хочете добавити зупинку? Зверніть увагу, якщо ви введете неіснуюче місце, зупинку буде добавлено у кінець

        if self.user_choice_route>0 and self.user_choice_route<=len(self.all_routes):
            if self.where_add_stop >0 and self.where_add_stop <= len(self.all_routes[self.user_choice_route - 1]): # чи місце додавання зупинки не менше, чим список зупинок певного маршруту
                self.all_routes[self.user_choice_route - 1].insert(where_add_stop-1, new_stop_name)  # додаємо зупинку у вказане місце вказаного маршруту
                print(f'Зупинку "{self.new_stop_name}" успішно додано у маршрут!')
            else:
                self.all_routes[self.user_choice_route - 1].append(new_stop_name) # додаємо зупинку у кінець вказаного маршруту
                print('Такого місця немає. Зупинку додано у кінець.')
        else:
            print('Такого маршруту не існує')

    def remove_stop(self, user_choice_stop, where_remove_stop):
        self.user_choice_stop = user_choice_stop # З якого маршруту видалити зупинку
        self.where_remove_stop = where_remove_stop # Яку зупинку видалити
        if self.user_choice_stop > 0 and self.user_choice_stop <= len(self.all_routes):
            if self.where_remove_stop > 0 and self.where_remove_stop <= len(self.all_routes[self.user_choice_stop - 1]):  # чи місце видалення зупинки не менше, чим список зупинок певного маршруту
                print(f'Зупинку "{self.all_routes[self.user_choice_stop - 1][where_remove_stop - 1]}" видалено')
                self.all_routes[self.user_choice_stop - 1].pop(where_remove_stop - 1)  # видаляємо зупинку з вказаного місця вказаного маршруту
            else:
                print('Такої зупинки не існує')
        else:
            print('Такого маршруту не існує')