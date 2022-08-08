from cgitb import html
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
from bs4 import BeautifulSoup

updater = Updater(BOT_TOKEN,use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text("Cómo estás? estás buscando un turno?")


def help(update: Update, context: CallbackContext):
    	update.message.reply_text("AIUUUUDAA")


def gmail_url(update: Update, context: CallbackContext):
    	update.message.reply_text("gmail link here")


def get_25_mayo(update: Update, context: CallbackContext):
    page = requests.get("https://turnos.clinica25demayo.com.ar/")
    

def get_dolar_price(update: Update, context: CallbackContext):
    page = requests.get("https://dolarhoy.com/cotizaciondolarblue")
    soup = BeautifulSoup(page.content, "html.parser")
    cot_mon_div = soup.find(class_="cotizacion_moneda")
    compra_div = cot_mon_div.find(class_='topic').find_next()
    venta_div = compra_div.find_next().find(class_='value')
    update.message.reply_text(f"Compra: {compra_div.text} - Venta: {venta_div.text}")


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('dolar', get_dolar_price))
updater.dispatcher.add_handler(CommandHandler('25_mayo', get_25_mayo))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	# Filters out unknown commands
	Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
