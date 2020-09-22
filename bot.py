import csv
import logging

import json
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

import os
import math
from csv import writer
import pandas as pd

import preprocessing as pp
import classification as clf

with open(os.path.join("C:/Users/Giaco/Desktop/TelegramBot", 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

token_api = secrets['BOT_TELEGRAM_KEY']


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TEXT, CANCEL = range(2)

def start(update, context):
    update.message.reply_text(
        'Hi! Send me a message, I\'ll tell you if is spam or ham in my opinion\n\n',
        reply_markup=ReplyKeyboardRemove())

    return TEXT

def analyze_text(sms):
    if (sms is None):
        return None
    global SMS, PREDICTED
    SMS = sms
    preprocessed_sms = pp.preprocess(sms)

    predicted = clf.classification(preprocessed_sms)
    PREDICTED = predicted
    return predicted


def text_classify(update, context):

    if(update.message.text == '/start'):
        start(update, context)
    logger.info("Computing %s", update.message.text)
    update.message.reply_text('Let me think...')

    predicted = analyze_text(update.message.text)

    keyboard = [[InlineKeyboardButton("Yes", callback_data='1'),
                 InlineKeyboardButton("No", callback_data='0')],
                [InlineKeyboardButton("I'm not sure enough", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if predicted:
        update.message.reply_text('For my humble opinion this is a SPAM message! Is it spam in your opinion?', reply_markup=reply_markup )
    else:
        update.message.reply_text('For my humble opinion this is a HAM message! Is it spam in your opinion?', reply_markup=reply_markup)

    update.message.reply_text('Rate the text if you want, also you can give me another text to classify or exit typing /cancel',
                              reply_markup=ReplyKeyboardRemove())

    return TEXT

def button(update, context):
    query = update.callback_query
    if query.data == "1":
        record = ["spam", SMS]
        with open('dataset/bot_dataset.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(record)
    elif query.data == "0":
        record = ["ham", SMS]
        with open('dataset/bot_dataset.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(record)
        print(record)
    query.edit_message_text(text="Thanks for your help! You're helping me to become the best version of myself")

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Cya, thanks for the great conversation',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main():
    updater = Updater(token_api, use_context=True)
    dp = updater.dispatcher
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            TEXT: [
                        MessageHandler(Filters.regex('^\/cancel'), cancel),
                        MessageHandler(Filters.regex('[^/]'), text_classify)
                    ]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()

def same_x(x):
  return x

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

if __name__ == '__main__':
    main()