class Home:
    def __init__(self, n_floors, name, date):
        self.n_floors = n_floors
        self.name = name
        self.date = date

    def __str__(self):
        return f'Количество этажей: {self.n_floors}\nНазваниедома: {self.name}\nГод построения: {self.date}'
