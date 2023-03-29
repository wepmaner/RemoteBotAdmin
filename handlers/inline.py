from aiogram import Router, F
from aiogram import types
from create_bot import bot
from config import admin_ids, services
import gui
import psutil
import methods
import callbackdata as cb

router = Router()
router.callback_query.filter(F.from_user.id.in_(admin_ids))

@router.callback_query(F.data=='menu')
async def menu(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    await bot.answer_callback_query(callback.id)
    await bot.edit_message_text('Меню:',chat_id,callback.message.message_id,reply_markup=gui.menu())

@router.callback_query(F.data=='service_list')
async def service_list(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    await bot.answer_callback_query(callback.id)
    await bot.edit_message_text('Список сервисов:',chat_id,callback.message.message_id,reply_markup=gui.get_services())

@router.callback_query(F.data=='server_info')
async def service_info(callback: types.CallbackQuery):
    chat_id = callback.message.chat.id
    await bot.answer_callback_query(callback.id)
    ram = psutil.virtual_memory()
    ram_used = round(ram.used / 1024**3,2)
    ram_total = round(ram.total / 1024**3,2)
    memory = psutil.disk_usage('/')
    memory_used = round(memory.used / 1024**3,2)
    memory_total = round(memory.total / 1024**3,2)

    text = f'''Информация

💾Оперативная память: {ram_used}/{ram_total}
💿Использовано памяти: {memory_used}/{memory_total}'''
    await bot.edit_message_text(text,chat_id,callback.message.message_id,reply_markup=gui.menu())

# Получение статуса сервиса
@router.callback_query(cb.Control.filter(F.action=='status'))
async def service_control(callback: types.CallbackQuery,callback_data:cb.Control):
    text = methods.get_status_low(callback_data.service)
    chat_id = callback.message.chat.id
    await bot.edit_message_text(text,chat_id,callback.message.message_id,reply_markup=gui.service_control(callback_data.service))

# Включение сервиса
@router.callback_query(cb.Control.filter(F.action=='start'))
async def service_control(callback: types.CallbackQuery,callback_data:cb.Control):
    methods.service_cmd('start',callback_data.service)
    text = methods.get_status_low(callback_data.service)
    chat_id = callback.message.chat.id
    await bot.edit_message_text(text,chat_id,callback.message.message_id,reply_markup=gui.service_control(callback_data.service))


# Выключение сервиса
@router.callback_query(cb.Control.filter(F.action=='stop'))
async def service_control(callback: types.CallbackQuery,callback_data:cb.Control):
    methods.service_cmd('stop',callback_data.service)
    text = methods.get_status_low(callback_data.service)
    chat_id = callback.message.chat.id
    await bot.edit_message_text(text,chat_id,callback.message.message_id,reply_markup=gui.service_control(callback_data.service))