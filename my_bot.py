from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define a function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main():
    # Replace 'YOUR_TOKEN' with the token provided by BotFather
    updater = Updater("7455282585:AAGLLwo5M--HS6kWTHnjDrCp0Ok1Ngn_Y-M", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()

    # Run the bot until you stop it with Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
