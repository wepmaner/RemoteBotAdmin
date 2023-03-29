from aiogram.filters.callback_data import CallbackData

class Control(CallbackData, prefix="service_control"):
    service: str
    action: str