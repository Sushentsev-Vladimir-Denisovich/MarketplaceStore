from telebot import TeleBot
bot = TeleBot('6234632894:AAFeXsjhbfMBrCkYsCiU-PQxzDW-a34Kots')


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "/start":
#         bot.send_message(message.from_user.id, "Здравствуйте!\n\nЯ бот онлайн магазина DwellWell. Пожалуйста, выберите, чем я могу вам помочь.")
#     elif message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    answer = "Тебе "+str(age)+" лет, тебя зовут "+name+" "+surname+"?"
    bot.send_message(message.from_user.id, answer)
    bot.register_next_step_handler(message, get_registration_answer);

def get_registration_answer(message):
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, "Отлично. Чем я могу тебе помочь, "+name)
    elif message.text.lower() == "нет":
        bot.send_message(message.from_user.id, "Тогда давай заново)\nКак тебя зовут?")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name


bot.polling(none_stop=True, interval=0)