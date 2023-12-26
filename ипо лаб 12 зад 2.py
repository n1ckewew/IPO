class Scanner:
    """Класс, описывающий сканеры"""
    def __init__(self, name, scanner_type, resolution, color_depth, interface_type, price):
        """Конструктор, выполняющий инициализацию атрибутов"""
        self.name = name
        self.scanner_type = scanner_type
        self.resolution = resolution
        self.color_depth = color_depth
        self.interface_type = interface_type
        self.price = price

    # Методы get и set для каждого атрибута
    # ...

    def __del__(self):
        """Деструктор"""
        print('Деструктор выполнился')

# Создание пустого списка и добавление в него сканеров и информации о них, которую ввёл пользователь
scanner_list=[]
for i in range(10):
    name=input('Введите название сканера  ')
    scanner_type=input('Введите тип сканера  ')
    resolution=int(input('Введите разрешение сканера  '))
    color_depth=int(input('Введите глубину цвета сканера  '))
    interface_type=input('Введите тип интерфейса сканера  ')
    price=int(input('Введите цену сканера  '))
    scanner=Scanner(name, scanner_type, resolution, color_depth, interface_type, price)
    scanner_list.append(scanner)

# Вывод всей информации о сканерах
for scanner in scanner_list:
    print('Название ', scanner.get_name())
    print('Тип ', scanner.get_scanner_type())
    print('Разрешение ', scanner.get_resolution())
    print('Глубина цвета ', scanner.get_color_depth())
    print('Тип интерфейса ', scanner.get_interface_type())
    print('Цена ', scanner.get_price())
    print()

del scanner_list
