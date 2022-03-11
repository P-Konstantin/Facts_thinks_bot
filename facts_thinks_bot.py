import telebot
import random
from telebot import types


# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()


# Загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close


# Создаем бота
bot = telebot.TeleBot('token')


# Команда start
@bot.message_handler(commands=['start'])
def start(m, res=False):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Факт')
    item2 = types.KeyboardButton('Поговорка')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми: "Факт" или "Поговорка"', reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        # Если юзер прислал 1, выдаем ему случайный факт
        if message.text.strip() == 'Факт':
            answer = random.choice(facts)
        elif message.text.strip() == 'Поговорка':
            answer = random.choice(thinks)
        # Отсылаем юзеру сообщение в его чат
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        answer = 'Нажмите "Факт" или "Поговорка" '
        bot.send_message(message.chat.id, answer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)


