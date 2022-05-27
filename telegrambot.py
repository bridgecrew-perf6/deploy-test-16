from telegram.ext import *
API_KEY=
print('Bot started')

def handle_message(update, context):
    text = str(update.messsage.text).lower()
    print(update)

    update.message.reply_text(f'Hi from Michael')

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(Message_Handler(Filter.text, handle_messsage))

    updater.start_polling(1.0)
    updater.idle()