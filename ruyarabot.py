import logging
from cevapuret import cevap # cevap ekleyen modülü ekliyoruz
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Rüyanızda gördüğünüz anahtar kelimeleri aralarına virgül ekleyerek yazınız\nÖrneğin bir rüyada kendinizi denizde yüzerken gördüyseniz deniz,yüz şeklinde kök hallerini yazınız.')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Rüyanızdaki anahtar kelimeleri aralarına virgül ekleyerek yazınız\nÖrneğin bir rüyada kendinizi denizde yüzerken gördüyseniz deniz,yüz şeklinde kök hallerini yazınız.')


def echo(update, context):
    with open("sayac.txt","r") as dosya:
        sayac=int(dosya.read())
    sayac+=1
    with open("sayac.txt","w",encoding="utf-8") as dosya:
        dosya.write(str(sayac))
    """Echo the user message."""
    update.message.reply_text(cevap(update.message.text)) #cevap yani tabir üreten sayfaya yönlendiriyoruz


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    token = "Buraya botunuzun tokeni eklenecek"
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
