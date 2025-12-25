import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start']) #декоратор к команде старт
def start_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться ❤️")
    btn2 = types.KeyboardButton("Как дела❓")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Привет! Выбери кнопку в меню 👇", reply_markup=markup)

# 2. Обработка текста (нажатия на нижние кнопки)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Поздороваться ❤️":
        bot.send_message(message.chat.id, "И тебе привет!")

    elif message.text == "Как дела❓":
        # Создаем Инлайн-кнопку (под сообщением)
        markup = types.InlineKeyboardMarkup() #обработчик любых текстовых сообщений
        btn_in1 = types.InlineKeyboardButton("Показать секрет 🐹", callback_data="secret_btn")
        markup.add(btn_in1) #добавил первую кнопку
        btn_in2 = types.InlineKeyboardButton("Или кинуть кубик, вдруг надо 🎲", callback_data="cube_btn") #callback_data="..."  - для обработки события нажатия на сообщение
        markup.add(btn_in2) # добавил вторую кнопку

        bot.send_message(message.chat.id, "Я просто бот, у меня нет дел, но есть кнопка:", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Я понимаю только нажатия кнопок...")

# 3. Обработка Инлайн-кнопок (callback)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "secret_btn":
        # Убираем часики загрузки на кнопке и показываем всплывающее уведомление
        bot.answer_callback_query(call.id, "Секрет раскрыт!", show_alert=True)

        # Можно также изменить исходное сообщение
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Секрет: Чуть обманул, тут нет ничего")
    elif call.data == "cube_btn":
        bot.answer_callback_query(call.id, "Кубик брошен🤯", show_alert=True) # отвечаем серверу, что кнопка сработала
        bot.send_dice(call.message.chat.id)




# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен")
    bot.infinity_polling()
