class Guests:
    def __init__(self, firstname, lastname, city, status):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.status = status

    def guest_information(self):
        print(f'Имя: {self.firstname} {self.lastname}, город: {self.city}, статус: {self.status}')

guest_1 = Guests('Иван', 'Иванов', 'Москва', 'Наставник')
guest_2 = Guests('Петр', 'Петров', 'Киев', 'Студент')
guest_3 = Guests('Лена', 'Ленина', 'Нью-Йорк', 'Куратор')
guest_4 = Guests('Катерина', 'Сидорова', 'Лондон', 'Студент')

guests = [guest_1, guest_2, guest_3, guest_4]
for guest in guests:
    guest.guest_information()