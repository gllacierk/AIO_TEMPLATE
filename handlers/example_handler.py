from loader import dp
from aiogram.types import Message


@dp.message_handler()
async def example_echo(message: Message):
    await message.answer(text=message.text)
