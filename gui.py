from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import services
import callbackdata as cb

def menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Сервисы',callback_data='service_list')
    keyboard.button(text='Информация о сервере',callback_data='server_info')
    keyboard.adjust(2)
    return keyboard.as_markup()

def get_services():
    keyboard = InlineKeyboardBuilder()
    for service in services:
        keyboard.button(text=service,callback_data=cb.Control(service=service,action='status'))
    keyboard.button(text='Главное меню',callback_data='menu')
    keyboard.adjust(3)
    return keyboard.as_markup()

def service_control(service):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Включить',callback_data=cb.Control(service=service,action='start'))
    keyboard.button(text='Выключить',callback_data=cb.Control(service=service,action='stop'))
    keyboard.button(text='Назад',callback_data='service_list')
    keyboard.button(text='Главное меню',callback_data='menu')
    keyboard.adjust(2)
    return keyboard.as_markup()
