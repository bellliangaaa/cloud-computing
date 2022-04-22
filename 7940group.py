from tkinter import N
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import configparser
import logging
import redis

import pymysql
dbinfo={"host":"192.168.10.237",
        "user":"root",
        "password":"12345",
        "db":"7940chatbot",
        "port":3306
}
global redis1

def main():
    # Load your token and create an Updater for your Bot
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher

    global redis1
    redis1 = redis.Redis(host=(config['REDIS']['HOST']), password=(config['REDIS']['PASSWORD']), port=(config['REDIS']['REDISPORT']))

    # You can set this logging module, so you will know when and why things do not work as expected
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    # register a dispatcher to handle message: here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # on different commands - answer in Telegram

    dispatcher.add_handler(CommandHandler("Lionrock", Lionrock))
    dispatcher.add_handler(CommandHandler("Boavista", Boavista))
    dispatcher.add_handler(CommandHandler("Longkewan", Longkewan))
    dispatcher.add_handler(CommandHandler("Oceanpoint", Oceanpoint))
    dispatcher.add_handler(CommandHandler("Lungshan", Lungshan))
    dispatcher.add_handler(CommandHandler("poguwan", poguwan))
    dispatcher.add_handler(CommandHandler("help", help))

    # To start the bot:
    updater.start_polling()
    updater.idle()


def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text= reply_message)


def help(update: Update, context: CallbackContext):
    update.message.reply_text('I am robot Ivan and I can provide information about hiking in Hong Kong ')
    update.message.reply_text('You can input ')
    update.message.reply_text('/lionrock   /poguwan   /longkewan    /oceanpoint   /lungshan   /boavista')
    update.message.reply_text('to get detailed information!')

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def Lionrock(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    
    sql1 = "select * from Route where routename = 'Lion rock';"
    connect1=pymysql.connect(**dbinfo)
    cursor1=connect1.cursor()
    cursor1.execute(sql1)
    r_all=cursor1.fetchall()
    update.message.reply_text(r_all)
    cursor1.close()
    connect1.close()
def a():
    print(1)

def Boavista(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    
    sql1 = "select * from Route where routename = 'Boa Vista';"
    connect1=pymysql.connect(**dbinfo)
    cursor1=connect1.cursor()
    cursor1.execute(sql1)
    r_all=cursor1.fetchall()
    update.message.reply_text(r_all)
    cursor1.close()
    connect1.close()
def b():
    print(1)
    
def Longkewan(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    sql1 = "select * from Route where routename = 'Long Ke Wan';"
    connect1=pymysql.connect(**dbinfo)
    cursor1=connect1.cursor()
    cursor1.execute(sql1)
    r_all=cursor1.fetchall()
    update.message.reply_text(r_all)
    cursor1.close()
    connect1.close()
def c():
    print(1)

def Oceanpoint(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    sql1 = "select * from Route where routename = 'Ocean Point';"
    connect1=pymysql.connect(**dbinfo)
    cursor1=connect1.cursor()
    cursor1.execute(sql1)
    r_all=cursor1.fetchall()
    update.message.reply_text(r_all)
    cursor1.close()
    connect1.close()
def d():
    print(1)

def Lungshan(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    sql1 = "select * from Route where routename = 'Lung Shan';"
    connect1=pymysql.connect(**dbinfo)
    cursor1=connect1.cursor()
    cursor1.execute(sql1)
    r_all=cursor1.fetchall()
    update.message.reply_text(r_all)
    cursor1.close()
    connect1.close()
def ed():
    print(1)
    
def poguwan(update: Update, context: CallbackContext) -> None:
    sql1 = "select * from Route where routename = 'Po Kwu Wan';"
    connect1=pymysql.connect(**dbinfo)
    cursor1=connect1.cursor()
    cursor1.execute(sql1)
    r_all=cursor1.fetchall()
    update.message.reply_text(r_all)
    cursor1.close()
    connect1.close()
    
    
    
if __name__ == '__main__':
    main()

