from telebot import TeleBot
from telebot import types

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
#Метод для обработки начала работы бота
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Давай познакомимся\nКак тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

#Метод для считывая и запоминания имени
def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

#Метод для считывая и запоминания фамилии
def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

#Метод для считывая и запоминания возраста
def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    #Реализация через сообщение
    # answer = "Тебе "+str(age)+" лет, тебя зовут "+name+" "+surname+"?"
    # bot.send_message(message.from_user.id, answer)
    # bot.register_next_step_handler(message, get_registration_answer);
    
    #Реализация через клавиатуру
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

#Метод для подтверждения корректности введенных регистрационных данных
def get_registration_answer(message):
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, "Отлично. Чем я могу тебе помочь, "+name)
    elif message.text.lower() == "нет":
        bot.send_message(message.from_user.id, "Тогда давай заново)\n\nКак тебя зовут?")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name

#Метод для обработки нажатий клавиш на клавиатуре
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, "Отлично. Чем я могу тебе помочь, "+name);
        bot.answer_callback_query(call.id, text="") #Устраняет проблему, что кнопка остается активной после нажатия на нее
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Тогда давай заново)\n\nКак тебя зовут?");
        bot.register_next_step_handler(call.message, get_name); #следующий шаг – функция get_name
        bot.answer_callback_query(call.id, text="") #Устраняет проблему, что кнопка остается активной после нажатия на нее

bot.polling(none_stop=True, interval=0)