import constants as const
import global_variables as gl

import random

from telebot import TeleBot
from telebot import types

bot = TeleBot('6234632894:AAFeXsjhbfMBrCkYsCiU-PQxzDW-a34Kots')

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == gl.admin_id:
        bot.send_message(gl.admin_id, const.start_message_for_admin);
    else:
        main_menu(message)

@bot.message_handler(commands=['help'])
def help(message):
    get_help(message)

@bot.message_handler(commands=['stop'])
def stop(message):
    if message.from_user.id == gl.admin_id:
        bot.stop_polling();
    else:
        bot.send_message(message.from_user.id, const.wait_start);


@bot.message_handler(content_types=['sticker'])
#Метод для обработки начала работы бота
def text_message(message):
    sticker_index = random.randint(0, len(const.stickers));
    bot.send_sticker(message.from_user.id, const.stickers[sticker_index])

@bot.message_handler(content_types=['text'])
#Метод для обработки начала работы бота
def text_message(message):
    #global user_id;

    if message.from_user.id == gl.admin_id:
        str_splitted = message.text.split(const.delimeter); # Разделяю сообщение от админа на массив строк для возможности ввода сообщения формата 1234%текст,
                                                #где "1234" - ID пользователя, которому нужно ответить, а "текст" - сообщение, отправленное ему
        if len(str_splitted) > 1:
            try:
                id = int(str_splitted[0]);
                bot.send_message(id, str_splitted[1]);
            except Exception:
                bot.send_message(gl.admin_id, const.incorrect_user_id);
        else:
            if (gl.user_id != 0):
                bot.send_message(gl.user_id, message.text);
            else:
                bot.send_message(gl.admin_id, const.not_user_id);
    else:
        bot.send_message(message.from_user.id, const.wait_start);

def get_help(message):
    bot.send_message(message.from_user.id, text="Для начала работы введите /start")

def main_menu(message):
    #global user_id;
    gl.user_id = message.from_user.id;
    #Реализация через клавиатуру
    keyboard = init_main_keyboard();
    bot.send_message(message.from_user.id, text=const.welcome_message, reply_markup=keyboard)

def back(call):
    keyboard = init_main_keyboard();
    bot.send_message(call.message.chat.id, text=const.welcome_message, reply_markup=keyboard)

# Метод для инициализации пользовательской клавиатуры
def init_main_keyboard():
    keyboard = types.InlineKeyboardMarkup();
    key_question = types.InlineKeyboardButton(text=const.keyboard_question, callback_data=const.clbk_question); #кнопка «Да»
    #keyboard.add(key_question); #добавляем кнопку в клавиатуру
    key_problem= types.InlineKeyboardButton(text=const.keyboard_problem, callback_data=const.clbk_problem);
    key_link_ozon= types.InlineKeyboardButton(text=const.keyboard_OZON_name, url = const.keyboard_OZON_URL, callback_data=const.clbk_ozon);
    key_link_wb= types.InlineKeyboardButton(text=const.keyboard_WB_name, url = const.keyboard_WB_URL, callback_data=const.clbk_wb);
    keyboard.row(key_question, key_problem);
    keyboard.row(key_link_ozon, key_link_wb);
    return keyboard;

# Метод для инициализации пользовательской клавиатуры
def init_additional_keyboard():
    keyboard = types.InlineKeyboardMarkup();
    key_back= types.InlineKeyboardButton(text=const.keyboard_back, callback_data=const.clbk_back);
    keyboard.add(key_back);
    return keyboard;

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
    if message.text == const.start:
        start(message);
    elif gl.current_clbk == const.clbk_question: # Если не сравнивать текущий callback с предусматриваемым в методе, то возникает проблема, что юзер может нажать одну кнопку, начать сценарий работы, а затем нажать другую и пойдут параллельно 2 сценария
        question = message.text;
        formatted_question = "Вопрос от пользователя: "+ str(message.from_user.id) + "\n\n" + question;
        bot.send_message(gl.admin_id, formatted_question);
        bot.register_next_step_handler(message, get_question);

#Метод для записи номера заказа
def get_order_number(message):
    if message.text == const.start:
        start(message);
    elif gl.current_clbk == const.clbk_problem:
        try:
            gl.order_number = int(message.text) #проверяем, что возраст введен корректно
            bot.send_message(gl.user_id, const.problem_message);
            bot.register_next_step_handler(message, get_problem);
        except Exception:
            bot.send_message(message.from_user.id, const.wait_number);
            bot.register_next_step_handler(message, get_order_number);

def get_problem(message):
    if message.text == const.start:
        start(message);
    else:
        problem = message.text;
        formatted_question = "Проблема от пользователя: "+ str(gl.user_id) + "\nНомер заказа: " + str(gl.order_number) + "\n\n" + problem;
        bot.send_message(gl.admin_id, formatted_question);
        bot.register_next_step_handler(message, get_problem);

#Метод для обработки нажатий клавиш на клавиатуре
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == const.clbk_question:
        #РАСКОММЕНИТИТЬ, ЧТОБ БЫЛА КЛАВИАТУРА "НАЗАД"
        #keyboard = init_additional_keyboard();
        #bot.send_message(call.message.chat.id, text=const.question_message, reply_markup=keyboard);
        gl.current_clbk = const.clbk_question;
        bot.send_message(call.message.chat.id, text=const.question_message);
        bot.register_next_step_handler(call.message, get_question); #следующий шаг – функция get_question
        bot.answer_callback_query(call.id, text="")
    elif call.data == const.clbk_problem:
        #РАСКОММЕНИТИТЬ, ЧТОБ БЫЛА КЛАВИАТУРА "НАЗАД"
        #keyboard = init_additional_keyboard();
        #bot.send_message(call.message.chat.id, const.order_nuber_message, reply_markup=keyboard);
        gl.current_clbk = const.clbk_problem;
        bot.send_message(call.message.chat.id, const.order_nuber_message);
        bot.register_next_step_handler(call.message, get_order_number); #следующий шаг – функция get_order_number
        bot.answer_callback_query(call.id, text="")
    elif call.data == const.clbk_back:
        back(call);
        bot.register_next_step_handler(call.message);

bot.polling(none_stop=True, interval=0)