import collections
import datetime

users = {}  # словарь пользователей

People = collections.namedtuple("people", ["name", "birthday"])  # кортеж описывающий друга


class FriendList:
    '''Класс описывающий список друзей конкретного пользователя'''

    def __init__(self):
        self.enabled = True
        self.friends = []

    def __getitem__(self, item):
        return self.friends[item]

    def __len__(self):
        return len(self.friends)

    def change_status(self, status: bool):
        self.enabled = status

    def append(self, people: list):
        '''Функция добавляющая нового человека в конец списка друзей'''
        name = people[0]
        birthday = people[1]
        self.friends.append(People(name, datetime.date(int(birthday[2]), int(birthday[1]), int(birthday[0]))))

    def show(self) -> str:
        '''Функция возвращающая текст содержащий всех друзей и их дни рождения'''
        current_day = datetime.date.today()
        text = [""] * ((len(self.friends)) * 3)  # каждый друг описывается 3 строчками
        i = 1  # номер друга в списке
        for people in self.friends:  # создание описания для каждого друга
            j = i * 3
            indent = " " * (len(str(i)) + 3)
            birthday = people[1]
            next_birthday = datetime.date(year=current_day.year + 1, month=birthday.month, day=birthday.day)
            waiting_time = (next_birthday - current_day).days % 365  # нужно придумать как учитывать весокосные года
            # (если они уже не учитываются)
            text[j - 3] = (f"{i}. {people[0]}")
            text[j - 2] = (indent + "Дата рождения - " + str(people[1]))
            text[j - 1] = (indent + "До дня рождения - " + str(waiting_time) + " дней")
            i += 1

        if not text:
            text = ["Тут пока пусто"]
        return "\n".join(text)

    def remove(self, number: int):
        '''Функция для удаления друга по номеру'''
        del self.friends[number]

    def multi_remove(self, numbers: list):
        '''Функция для удаления нескольких друзей по номерам'''
        numbers = set(numbers)
        new_friends = []
        for i in range(len(self.friends)):
            if i not in numbers:
                new_friends.append(self.friends[i])
        self.friends = new_friends

    def current_birthdays(self, day: datetime.date) -> list:
        "Функция возвращающая список имён у которых день рождения в выбранный день"
        result = []
        for p in self.friends:
            if p[1].month == day.month and p[1].day == day.day:
                result.append(p[0])
        return result
