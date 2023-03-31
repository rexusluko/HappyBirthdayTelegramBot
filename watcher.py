import datetime


def happy_birthday(user, birthday_persons, telegram_bot):
    '''Функция рассылающая пользователю уведомления'''
    birthday_persons_total = len(birthday_persons)
    if birthday_persons_total == 0:
        pass
    elif birthday_persons_total == 1:
        telegram_bot.send_message(chat_id=user, text=f"Сегодня день рождения у {birthday_persons[0]}!")
    else:
        telegram_bot.send_message(chat_id=user, text=f"Сегодня день рождения у {birthday_persons_total} твоих друзей!")
        text = ", ".join(birthday_persons[:-1]) + " и " + birthday_persons[-1]
        telegram_bot.send_message(chat_id=user, text=f"В их числе {text}!")


def check(users, bot):
    '''Функция проверяющая даты рождений'''
    current_day = datetime.date.today()
    for user, user_info in zip(users.keys(), users.values()):
        if user_info[1].enabled:
            happy_birthday(user, user_info[1].current_birthdays(current_day), bot)
