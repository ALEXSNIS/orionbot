import telebot
from telebot import types
bot = telebot.TeleBot("5601290602:AAHoIGxXJ1fRqIMUQhczjlmCfI-bDL7W8C4")
admin=telebot.TeleBot('5647554251:AAG5JzgyN3AUabz5CJZGdjeFlJtYm4obQBY')
class User_info(object):
    Name=str
    Curse=str
    Phone=str
def send():
    admin.send_message(-1001560084700,f'{User_info.Curse}\n'
                                  f'Name:{User_info.Name}\n'
                                  f'Phone: {User_info.Phone}')
@bot.message_handler(commands=['start'])
def start(message):
    nav(message)
    bot.send_message(message.chat.id,f'Здраствуйте <b>{message.from_user.first_name}</b>. Здесь вы можете узнать и записаться на курсы в Orion School', parse_mode='html')
def nav(message):
    markup = types.ReplyKeyboardMarkup()
    front = types.KeyboardButton('Front-end')
    full = types.KeyboardButton('Fullstack')
    about = types.KeyboardButton('О нас')
    markup.row(front, full)
    markup.row(about)
    bot.send_message(message.chat.id, 'Выберите курс', reply_markup=markup)
@bot.message_handler()
def get_user_text(message):
    markup=types.ReplyKeyboardMarkup()
    infoFront=types.KeyboardButton('Детальней про Front-end')
    SharePhone=types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    infoFull=types.KeyboardButton('Детальней про Fullstack')
    join=types.KeyboardButton('Присоединится к курсам')
    cansel=types.KeyboardButton('Cancel')
    front = types.KeyboardButton('Курс по Front-end')
    full = types.KeyboardButton('Курс по Fullstack')
    if message.text=="О нас":
        bot.send_message(message.chat.id,'Orion School',parse_mode=None)
    elif message.text=="Front-end":
        markup.row(infoFront, join)
        markup.row(cansel)
        bot.send_message(message.chat.id,'Курс Front-end\n'
                                         'Преподаватель: Игорь Гненный\n'
                                         'Продолжительность: 6 месяцев\n'
                                         'Стоимость: 2500 грн в месяц - 15000 грн за весь курс',reply_markup=markup)
    elif message.text=="Fullstack":
        markup.row(infoFull, join)
        markup.row(cansel)
        bot.send_message(message.chat.id,'Курс Fullstack\n'
                                         'Преподаватель: Игорь Гненный\n'
                                         'Продолжительность: 1 год\n'
                                         'Стоимость: 3000 грн в месяц - 36000 грн за весь курс',reply_markup=markup)
    elif message.text=="Cancel":
        nav(message)
    elif message.text=='Детальней про Front-end':
        doc=open('./info/Front-end.pdf','rb')
        bot.send_document(message.chat.id,doc)
    elif message.text=='Детальней про Fullstack':
        doc = open('./info/Fullstack.pdf', 'rb')
        bot.send_document(message.chat.id, doc)
    elif message.text=='Присоединится к курсам':
        markup.row(front,full)
        bot.send_message(message.chat.id,'Благодорим за то что выбрали нас:)\nВы не пожалеете')
        bot.send_message(message.chat.id,'Какой курс выбрали?',reply_markup=markup)
    elif message.text=="Курс по Front-end" or message.text=="Курс по Fullstack":
        User_info.Curse=message.text
        bot.send_message(message.chat.id, 'Отправте номер телефона что мы могли созвонится с вами',
                         reply_markup=markup.add(SharePhone))
    else:
        bot.send_message(message.chat.id,'Пожалуйста нажмите на кнопки внизу',parse_mode=None)
@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        User_info.Phone=message.contact.phone_number
        firstName=message.contact.first_name
        lastName=message.contact.last_name
        nav(message)
        if lastName is not None:
            User_info.Name=f'{firstName} {lastName}'
        else:
            User_info.Name=firstName
    send()
bot.polling(none_stop=True)