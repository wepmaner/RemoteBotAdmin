from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import config

storage = MemoryStorage()

bot = Bot(token=config.token)
dp = Dispatcher()