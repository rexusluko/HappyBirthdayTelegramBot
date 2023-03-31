import re
from classes import users

def remove(update, context):
    '''1 этап добавления друга в список'''
    global users
    id = update.effective_chat.id
    context.bot.send_message(chat_id=id,
                             text=users[id][1].show())
    context.bot.send_message(chat_id=id,
                             text="Напишите номера друзей для удаления через запятую(Например: 1,2,3,4)")
    context.bot.send_message(chat_id=id,
                             text="Или через тире (Например: 1-4)")
    return "remove1"


def remove1(update, context):
    global users
    id = update.effective_chat.id
    text = update.message.text
    if "".join(re.findall(r"\d+-\d+", text)) == text:
        slice=re.findall(r"\d+-\d+", text)[0]
        dash=slice.find("-")
        print(range(int(slice[:dash]),int(slice[dash+1:])+1))
        users[id][1].multi_remove(range(int(slice[:dash])-1,int(slice[dash+1:])))
    elif "".join(re.findall(r"\d+", text)):
        numbers=[]
        for n in re.findall(r"\d+", text):
            numbers.append(int(n)-1)
        users[id][1].multi_remove(numbers)
    else:
        context.bot.send_message(chat_id=id,
                                 text="Вы неправильно выбрали номера")
        context.bot.send_message(chat_id=id,
                                 text="Напишите номера друзей для удаления через запятую(Например: 1,2,3,4)")
        context.bot.send_message(chat_id=id,
                                 text="Или через тире (Например: 1-4)")
        return "remove1"
    context.bot.send_message(chat_id=id,
                             text="Я удалил выбранных друзей")
    context.bot.send_message(chat_id=id,
                             text=users[id][1].show())
    return "BASE"
