import constants as const

from telebot import TeleBot
from telebot import types

bot = TeleBot('6234632894:AAFeXsjhbfMBrCkYsCiU-PQxzDW-a34Kots')

# ИЗМЕНИТЬ КЛАВИАТУРУ, ЧТОБ БЫЛО НЕ 4 КНОПКИ В КОЛОНКУ, А 2 КОЛОНКИ ПО 2 КНОПКИ
# ДОБАВИТЬ ССЫЛКИ НА OZON, WB

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
admin_id = 616381025;
user_id = 0;

@bot.message_handler(content_types=['text'])
#Метод для обработки начала работы бота
def start(message):
    global user_id;

    if message.from_user.id == admin_id:
        str_splitted = message.text.split(const.delimeter); # Разделяю сообщение от админа на массив строк для возможности ввода сообщения формата 1234%текст,
                                                #где "1234" - ID пользователя, которому нужно ответить, а "текст" - сообщение, отправленное ему
        if len(str_splitted) > 1:
            try:
                id = int(str_splitted[0]);
                bot.send_message(id, str_splitted[1]);
            except Exception:
                bot.send_message(admin_id, const.incorrect_user_id);
        else:
            if (user_id != 0):
                bot.send_message(user_id, message.text);
            else:
                bot.send_message(admin_id, const.not_user_id);
    else:
        if message.text == '/start':
            user_id = message.from_user.id;
            #Реализация через клавиатуру
            keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
            key_question = types.InlineKeyboardButton(text=const.keyboard_question, callback_data=const.clbk_question); #кнопка «Да»
            #keyboard.add(key_question); #добавляем кнопку в клавиатуру
            key_problem= types.InlineKeyboardButton(text=const.keyboard_problem, callback_data=const.clbk_problem);
            key_link_ozon= types.InlineKeyboardButton(text=const.keyboard_OZON_name, url = const.keyboard_OZON_URL, callback_data=const.clbk_ozon);
            key_link_wb= types.InlineKeyboardButton(text=const.keyboard_WB_name, url = const.keyboard_WB_URL, callback_data=const.clbk_wb);
            keyboard.row(key_question, key_problem);
            keyboard.row(key_link_ozon, key_link_wb);
            bot.send_message(message.from_user.id, text=const.welcome_message, reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, 'Напиши /start');

#Метод для считывая и запоминания имени
def get_name(message):
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
            bot.register_next_step_handler(message, get_age);
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

#Метод для отправки вопроса от пользователя к админу
def get_question(message):
    question = message.text;
    formatted_question = "Вопрос от пользователя: "+ str(message.from_user.id) + "\n\n" + question;
    bot.send_message(admin_id, formatted_question);
    bot.register_next_step_handler(message, get_answer_for_question);

#Метод для отправки ответа от админа пользователю
def get_answer_for_question(message):
    bot.send_message(message.from_user.id, message.text);
    bot.register_next_step_handler(message, get_question);

#Метод для подтверждения корректности введенных регистрационных данных
# def get_registration_answer(message):
#     if message.text.lower() == "да":
#         bot.send_message(message.from_user.id, "Отлично. Чем я могу тебе помочь, "+name)
#     elif message.text.lower() == "нет":
#         bot.send_message(message.from_user.id, "Тогда давай заново)\n\nКак тебя зовут?")
#         bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name

#Метод для обработки нажатий клавиш на клавиатуре
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, "Отлично. Чем я могу тебе помочь, "+name);
        bot.answer_callback_query(call.id, text="") #Устраняет проблему, что кнопка остается активной после нажатия на нее
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Тогда давай заново)\n\nКак тебя зовут?");
        bot.register_next_step_handler(call.message, get_name); #следующий шаг – функция get_name
        bot.answer_callback_query(call.id, text="")
    elif call.data == const.clbk_question:
        bot.send_message(call.message.chat.id, "Пожалуйста, задайте мне свой вопрос. Я отправлю его менеджеру и перешлю ответ");
        bot.register_next_step_handler(call.message, get_question); #следующий шаг – функция get_name
        bot.answer_callback_query(call.id, text="")

bot.polling(none_stop=True, interval=0)