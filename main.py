class WARRIOR():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color


    def sleep(self):
        return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} ест')
        self.power += 1

    def hit(self):
        return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} ударил')
        self.endurance -= 1

    def wolk(self):
        return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} гуляет')
        self.endurance -= 1

    def info(self):
        return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'имя -{self.name}, сила - {self.power}, выносливость - {self.endurance}, цвет волос {self.hair_color}')
        