from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import types
from config import admin_ids
import psutil
from datetime import datetime
import subprocess
import logging
import gui
import methods

logger = logging.getLogger('commands')
router = Router()
router.message.filter(F.from_user.id.in_(admin_ids))

@router.message(Command(commands=['start']))
async def start(message:types.Message):
    await message.answer(f'Список сервисов:',reply_markup=gui.menu())
