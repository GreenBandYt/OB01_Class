class WARRIOR():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color


    def sleep(self):
        #return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        #return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} ест')
        self.power += 1

    def hit(self):
        #return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} ударил')
        self.endurance -= 1

    def wolk(self):
        #return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'{self.name} гуляет')
        self.endurance -= 1

    def info(self):
        return f'{self.name} {self.power} {self.endurance} {self.hair_color}'
        print(f'имя - {self.name}, сила - {self.power}, выносливость - {self.endurance}, цвет волос - {self.hair_color}')


war1 = WARRIOR('Варвар', 100, 50, 'черный')
war2 = WARRIOR('Викинг', 150, 100, 'седой')

print(war1.info())
print(war2.info())

war1.sleep()
war2.eat()
war1.hit()
war2.wolk()
war1.eat()

print(war1.info())
print(war2.info())

# !!!   FOR LATEST CODING  !!!