import telebot
import config
import requests
from verifier import is_khnu_page
import data

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def set_start(message):
    bot.send_message(message.chat.id, 'Start news')

@bot.message_handler(commands=['send'])
def send_pages(message):
    domenParams = data.list_of_available_sites['https://www.khnu.km.ua']
    url = 'https://www.khnu.km.ua' + domenParams[0] + str(domenParams[1])
    response = requests.get(url)
    if is_khnu_page(response.text):
       bot.send_message(message.chat.id, url)

@bot.message_handler(commands=['list'])
def get_list_sites(message):
    if len(data.list_of_available_sites) > 0:
        response = 'List of available sites:'
        for key in data.list_of_available_sites:
            response += '\n' + key
        bot.send_message(message.chat.id, response, True)
    else:
        bot.send_message(message.chat.id, 'List is empty')

        

bot.polling()