import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import TOKEN

bot = Bot(token=TOKEN, parse_mode="HTML")       # Обект бота
storage = MemoryStorage()                       # Объект памяти
dp = Dispatcher(bot=bot, storage=storage)       # Обект Dispatcher`a

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)