import re
import datetime
from classes import users


def add(update, context):
    '''1 этап добавления друга в список'''
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Введите имя друга")
    return "add1"


def add1(update, context):
    '''2 этап добавления друга в список'''
    global users
    id = update.effective_chat.id
    if len(re.findall(r"\d+", update.message.text)) != 0:
        context.bot.send_message(chat_id=id,
                                 text=f"Вы ввели недопустимое имя(оно содержит цифры)")
        context.bot.send_message(chat_id=id,
                                 text="Введите имя друга")
        return "add1"
    users[update.effective_chat.id][0][0] = update.message.text
    context.bot.send_message(chat_id=id,
                             text=f"Теперь введите дату рождения в формате D.M.YYYY")
    return "add2"


def add2(update, context):
    '''3 этап добавления друга в список'''
    global users
    id = update.effective_chat.id
    new_date = update.message.text.split(".")
    try:
        datetime.date(day=int(new_date[0]), month=int(new_date[1]), year=int(new_date[2]))
    except:
        context.bot.send_message(chat_id=id,
                                 text=f"Такой даты не существует")
        context.bot.send_message(chat_id=id,
                                 text=f"Теперь введите дату рождения в формате D.M.YYYY")
        return "add2"
    user = users[id]
    user[0][1] = new_date
    user[1].append(user[0])
    context.bot.send_message(chat_id=id,
                             text=f"Сейчас я отслеживаю {len(user[1])} твоих друзей. В их числе теперь {user[0][0]}")
    return "BASE"
