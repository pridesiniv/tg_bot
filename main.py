import logging
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_bot(updater: Updater, context: CallbackContext):
    print(updater)
    mytxt = f'Hello {updater.message.chat.first_name}'
    updater.message.reply_text(mytxt)


def main():
    upd = Updater('your TOKEN')
    upd.dispatcher.add_handler(CommandHandler("start", start_bot))
    upd.start_polling()
    upd.idle()


if __name__ == '__main__':
    logging.info('bot started!')
    main()
