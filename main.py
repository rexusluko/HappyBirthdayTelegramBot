# token = 5381690093:AAEkO8K_cpV2yzc5Ni_mlMEO5IUhb5cLV2w
import telegram

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import logging
    import time
    import schedule
    import collections
    import datetime


    from telegram.ext import ExtBot, Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

    from classes import People,FriendList,users
    from basic_commands import start,change_status,show,unknown,help
    from add_commands import add,add1,add2
    from watcher import check
    from remove_commands import remove,remove1

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)


    TOKEN = '5381690093:AAEkO8K_cpV2yzc5Ni_mlMEO5IUhb5cLV2w'
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    bot = ExtBot(token=TOKEN)
    all_handler = ConversationHandler(
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # словарь состояний разговора, возвращаемых callback функциями
        states={
            "BASE":[
                CommandHandler('show', show),
                CommandHandler('change_status', change_status),
                MessageHandler(filters=~Filters.command, callback=unknown),
                CommandHandler('add', add),
                CommandHandler('help', help),
                CommandHandler('remove', remove)
            ],

            # Этап `FIRST` - т.е. функция обработчик какого то сообщения явно
            # вернула константу FIRST (return `FIRST`), а так же послала/ответила
            # на сообщение. Ответ пользователя на это сообщение будет
            # обрабатываться обработчиками определенными в этом списке
            "add1": [
                MessageHandler(Filters.text, add1)
            ],
            # Этап `SECOND` - происходит то же самое, что и в описании этапа `FIRST`
            "add2": [
                MessageHandler(Filters.text, add2)
            ],
            "remove1":[MessageHandler(Filters.text, remove1)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('add', add)],
    )
    dispatcher.add_handler(all_handler)

    updater.start_polling()  # включение бота

    schedule.every().day.do(check, users,bot)  # каждый день проверять дни рождений
    while True:
        schedule.run_pending()
        time.sleep(1)