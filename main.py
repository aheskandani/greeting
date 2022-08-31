from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


TOKEN = '5127644377:AAFBXg8DEizQPWi0aYECgtFHQB6GMtu7Qs8'

updater = Updater(TOKEN, use_context=True)

# Bot commands
def start(update: Update, context: CallbackContext):
	update.message.reply_text('Hello friend 🙏🏻')

def id(update: Update, context: CallbackContext):
	update.message.reply_text(f'Chat ID: {update.message.chat_id}')

def other(update: Update, context: CallbackContext):
    pass

if __name__ == '__main__':
	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('id', id))
	updater.dispatcher.add_handler(MessageHandler(Filters.text, other))
	updater.dispatcher.add_handler(MessageHandler(Filters.command, other))
	updater.dispatcher.add_handler(MessageHandler(Filters.text, other))
	updater.start_polling()