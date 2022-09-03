import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import id_cred_bot

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print("Вызван /Start")
    update.message.reply_text("Привет человек")
def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(id_cred_bot.API_KEY)
        
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот взлетел")
    mybot.start_polling()
    mybot.idle()

main()
