import asyncio
from aiogram import Bot, Dispatcher
from handlers import router 
# from handlers import router as intelligence_router
from buttons import robots_inline
from buttons import intelligence_inline, conscious_inline
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


API_TOKEN = "8025828818:AAFhIiLB4EJ5WW8I2OtOtStFZKPGVqogoPo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
dp.include_router(router)
# dp.include_router(intelligence_router)



# Main menu keyboard
robot_button = InlineKeyboardButton(text="Robot Button", callback_data="robot_list_button")
ethics_button = InlineKeyboardButton(text="Robot Ethics", callback_data="ethics_robot")
intelligence_button = InlineKeyboardButton(text="Intelligence Theories", callback_data="intelligence_button")
conscious_button = InlineKeyboardButton(text="Consciousness Theories", callback_data="conscious_button")
keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[[robot_button, ethics_button], [intelligence_button],
    [conscious_button]])


# Start command
@dp.message(lambda message: message.text == "/start")
async def start_command(message):
    await message.answer("Hello! I am Her. How can I help you today?", reply_markup=keyboard_inline)


# Help command
@dp.message(lambda message: message.text == "/help")
async def help_command(message):
    await message.answer("Hello. This is About Her robot helps you to get understanding about Humanoid Robots!")


# Robot list button handler
@router.callback_query(lambda cb: cb.data == "robot_list_button")
async def robot_list_handler(callback_query: CallbackQuery):
    await callback_query.message.answer("You selected Robot's button", reply_markup=robots_inline)
    await callback_query.answer()

@router.callback_query(lambda cb: cb.data == "intelligence_button")
async def intelligence_handler(callback_query: CallbackQuery):
    await callback_query.message.answer("You selected Intelligence Theory section", reply_markup=intelligence_inline)
    await callback_query.answer()

@router.callback_query(lambda cb: cb.data == "conscious_button")
async def conscious_handler(callback_query: CallbackQuery):
    await callback_query.message.answer("You selected Consciousness Theories button", reply_markup=conscious_inline)
    await callback_query.answer()

# Main function
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
