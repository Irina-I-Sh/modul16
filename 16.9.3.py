class Customer:
    def __init__(self, firstname, lastname, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def customer_information(self):
        print(f'Клиент: {self.firstname} {self.lastname}, Баланс: {self.balance} руб.')

customer_1 = Customer ('Иван', 'Петров', 50)
customer_2 = Customer ('Петр', 'Иванов', 25)

customers = [customer_1, customer_2]
for customer in customers:
    customer.customer_information()