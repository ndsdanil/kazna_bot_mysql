from mysql_connector import Mysql_connector
from telebot import types

class Income:
    
    def __init__(self, bot):
        self.bot = bot 

    def info_message_income(self, message):
        self.bot.send_message(message.chat.id, "You chose Income, please, incert the number of Income")
        self.bot.register_next_step_handler(message, self.set_income)
    
    def set_income(self, message):
        self.user_income_number = message.text
        self.bot.send_message(message.chat.id, "You inserted your income, now please insert the source of Income: ")  
        self.bot.register_next_step_handler(message, self.set_income_source)   
    
    def set_income_source(self, message):
        self.user_income_source = message.text
        markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        options = ['cash_euro_with_me', 'cash_euro_not_with_me', 'cash_$_with_me', 'cash_$_not_with_me', 'card_euro', 'card_$', 'cash_(RUB)_not_with_me', 'card_(RUB)', 'bitcoin', 'shares(RUB)']
        buttons = [types.KeyboardButton(option) for option in options]
        markup.add(*buttons)
        self.bot.send_message(message.chat.id, "You set the income source, please set the income column", reply_markup=markup)
        self.bot.register_next_step_handler(message, self.set_income_column)
    
    def set_income_column(self, message):
        self.user_income_column = message.text
        print('value = '+ self.user_income_number)
        print('now we wil test incoming values from income class, column and income number' + str(self.user_income_column) + ' ' + self.user_income_number)
        Mysql_connector.insert_sql_query('Income', self.user_income_source, self.user_income_column, self.user_income_number)
        self.bot.send_message(message.chat.id, "You inserted income entry succesfully ")   
        





