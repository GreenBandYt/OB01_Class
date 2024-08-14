# New Questions on Lessons:
# Разберем задачу с простой учетной системой банка.

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance


    def deposit(self, money):
        self.balance += money
        print(f'Вы успешно пополнили счет. Текущая сумма: {self.balance}')


    def withdraw(self, money):
        if self.balance < money:
            print('Недостаточно средств.')
        else:
            self.balance -= money
            print(f'Вы успешно сняли средства {money}. Текущая сумма: {self.balance}')


    def get_balance(self):
        print(f'Текущая сумма: {self.balance}')


man = Account("1", 100)


man.get_balance()
man.withdraw(150)
man.get_balance()
man.deposit(200)
man.get_balance()
