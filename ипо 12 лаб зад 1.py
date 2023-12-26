class Student:#создание класса студент
    def __init__(self, surname, initials, group, uspev):#инициализация полей
        self.surname=surname
        self.initials=initials
        self.group=group
        self.uspev=uspev
#создание списка студентов и ввод информации о студентах
students=[]
for i in range(5):
    surname=input('Введите фамилию студента  ')
    initials=input('Введите инициалов студента  ')
    group=input('Введите номер группы студента  ')
    #создания пустого списка для записи и добавления отметок студента
    uspev=[]
    for j in range(5):
        mark=int(input('Введите оценку студента  '))
        uspev.append(mark)
    student=Student(surname, initials, group, uspev)
    students.append(student)
found=False
for student in students:#проверка списка на наличие у студентов неудовлетворительных отметок, если есть выводит фамилию и группу
    if any(mark < 3 for mark in student.uspev):
        print('Фамилия: ',student.surname,'группа:', student.group, 'студента с неудовлетворительной отметкой')
        found=True
if not found:#в случае отсутствия таких студентов выводт сообщение
    print('Нет студентов с неудовлетворительными отметками ')