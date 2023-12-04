class Circus:
    def __init__(self, name, city, premiere_date, duration_period, ticket_price, author, genre, num_actors):
        self.name = name
        self.city = city
        self.premiere_date = premiere_date
        self.duration_period = duration_period
        self.ticket_price = ticket_price
        self.author = author
        self.genre = genre
        self.num_actors = num_actors
    def __str__(self):
        return f"Circus: {self.name}\nCity: {self.city}\nPremiere Date: {self.premiere_date}\nDuration Period: {self.duration_period}" \
            f"\nTicket Price: {self.ticket_price}\nAuthor: {self.author}\nGenre: {self.genre}\nNumber of Actors: {self.num_actors}"
class AcrobaticPerformance(Circus):
    def __init__(self, name, city, premiere_date, duration_period, ticket_price, author, genre, num_actors, acrobatics_type, equipment):
        super().__init__(name, city, premiere_date, duration_period, ticket_price, author, genre, num_actors)
        self.acrobatics_type = acrobatics_type
        self.equipment=equipment
    def __str__(self):
        return super().__str__() + f"\nAcrobatics Type: {self.acrobatics_type}\nEquipment: {self.equipment}"
class AnimalTraining(Circus):
    def __init__(self, name, city, premiere_date, duration_period, ticket_price, author, genre, num_actors, training_type, num_animals):
        super().__init__(name, city, premiere_date, duration_period, ticket_price, author, genre, num_actors)
        self.training_type = training_type
        self.num_animals = num_animals
def __str__(self):
    return super().__str__() + f"\nTraining Type: {self.training_type}\nNumber of Animals: {self.num_animals}"

class MagicShow(Circus):
    def __init__(self, name, city, premiere_date, duration_period, ticket_price, author, genre, num_actors, magic_type, equipment):
        super().__init__(name, city, premiere_date, duration_period, ticket_price, author, genre, num_actors)
        self.magic_type = magic_type
        self.equipment = equipment

def __str__(self):
    return super().__str__() + f"\nMagic Type: {self.magic_type}\nEquipment: {self.equipment}"

circus_1=Circus("Фокусы", "Нью Йорк", "2022-05-10", "1 месяц", "50 рублей", "Джозеф Джостар", "Комедия", 20)
acrobatics_1=AcrobaticPerformance("Акробатическое шоу", "Рим", "2022-06-15", "2 недели", "40 долларов", "Монке Д Луффи", "Драма", 15,
"Group Acrobatics", "Poles, Trampolines")
animal_training_1=AnimalTraining("Дрессировка животных ", "Лондон", "2022-07-20", "3 месяца", "$60", "Джонатан Джостар", "Приключения", 25,
"Large Animals", 8)
print(circus_1)
print("\n")
print(acrobatics_1)
print("\n")
print(animal_training_1)





