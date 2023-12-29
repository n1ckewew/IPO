class House:
    def __init__(self, address, floors, rooms, color):
        self._address = address
        self._floors = floors
        self._rooms = rooms
        self._color = color

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, str):
            self._address = value
        else:
            print("Адрес должен быть строкой")

    @property
    def floors(self):
        return self._floors

    @floors.setter
    def floors(self, value):
        if isinstance(value, int):
            self._floors = value
        else:
            print("Количество этажей должно быть целым числом")

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        if isinstance(value, int):
            self._rooms = value
        else:
            print("Количество комнат должно быть целым числом")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = value
        else:
            print("Цвет должен быть строкой")
house = House("ул. Пушкина, д. Колотушкина", 2, 5, "красный")
print(house.address)  # ул. Пушкина, д. Колотушкина
house.floors = 3  # Изменяем количество этажей
print(house.floors)  # 3
house.rooms = "пять"  # Попытка присвоить некорректное значение вызовет ошибку
