import telebot
bot = telebot.TeleBot("947175267:AAG9p0K_h708ZaLBBjj3pTsYTa3aANxbBa0")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,  "Служба заказа готовых блюд и программа лояльности ресторанов в Telegram на базе коробочного решения FastBOT!")
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Меню📄', 'Корзина🍱')
    user_markup.row('Профиль🙍‍♂️', 'Помощь💬')
    bot.send_message(message.from_user.id, 'Добро пожаловать,!\n\nНажмите копнку Меню, что бы сделать заказ блюд.В своем Профиле Вы сможете посмотреть предыдущие заказы и повторить их еще раз!', reply_markup=user_markup)
bot.polling(none_stop=True)
