from classes import People, FriendList, users


def start(update, context):
    '''Функция реализующая комманду /start у телеграм бота'''
    global users
    user_id = update.effective_chat.id
    users[user_id] = [["", []], FriendList()]  # каждый юзер содержит в себе заготовку нового друга и
    # класс хранящий список его друзей
    context.bot.send_message(chat_id=user_id,
                             text="Привет! Я бот, который будет напоминать тебе о днях рождения твоих друзей")
    context.bot.send_message(chat_id=user_id,
                             text="Сейчас у тебя нет друзей за которыми я буду следить. Попробуй их добавить "
                                  "с помощью комманды /add ")
    return "BASE"


def change_status(update, context):  # функция для вкл/выкл слежки за днями рождения ( /change_status )
    '''Функция реализующая комманду /change_status у телеграм бота

    Отключает либо включает отслеживание дней рождений

    '''
    global users
    user_id = update.effective_chat.id
    if users[user_id][1].enabled:
        users[user_id][1].change_status(False)
        text = "Я больше не буду напомоминать о днях рождения"
    else:
        users[user_id][1].change_status(True)
        text = "Теперь я буду напоминать о днях рождения"
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)
    return "BASE"


def show(update, context):  # функция для отображения списка друзей ( /show )
    '''Функция реализующая комманду /show у телеграм бота'''
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=users[update.effective_chat.id][1].show())
    return "BASE"


def unknown(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вы ввелли что-то непонятное")
    context.bot.send_message(chat_id=chat_id,
                             text="Попробуйте использовать комманду /help чтобы узнать о командах бота")
    return "BASE"


def help(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,
                             text="Список комманд")
    return "BASE"
