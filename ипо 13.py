class Drob(object):#создание класса дробь
    """ Дробь вида a/b"""
    def __init__(self, a=0, b=1):#инициализация аргументов
        self.a = a
        self.b = b
        self.normalize()

    def normalize(self):
        """ Приводит дробь вида 4/6 к 2/3"""
        gcd = self.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def gcd(self, a, b):
        """ Находит наибольший общий делитель"""
        while b != 0:
            a, b = b, a % b
        return a

    def __str__(self):#установка формата и возврат его
        return '{}/{}'.format(self.a, self.b)

    def __eq__(self, other):#равно и возврат ответа
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):#меньше чем и возврат ответа
        return self.a * other.b < other.a * self.b

    def __add__(self, other):#сумма и возврат овета
        a = self.a * other.b + self.b * other.a
        b = self.b * other.b
        return Drob(a, b)

    def __sub__(self, other):#вычитание и возврат ответа
        a = self.a * other.b - self.b * other.a
        b = self.b * other.b
        return Drob(a, b)

    def __mul__(self, other):#умножение и возврат ответа
        a = self.a * other.a
        b = self.b * other.b
        return Drob(a, b)

    def __truediv__(self, other):#деление и возврат ответа
        a = self.a * other.b
        b = self.b * other.a
        return Drob(a, b)

# проверка
d1 = Drob(2, 3)
d2 = Drob(3, 4)
d3 = Drob(4, 6)
print(d1)
print(d2)
print(d3)
print(d1 == d2) # False
print(d1 == d3) # True
print(d1 < d2) # True
print(d1 > d2) # False
print(d1 + d2)
print(d1 - d2)
print(d1 * d2)
print(d1 / d2)