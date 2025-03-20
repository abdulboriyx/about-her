import json
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


# load data from JSON file
with open("robots.json", "r") as file:
      json_file = json.load(file)

# class
class Her:
      def __init__(self, data):
            self.data = data
      def get_robot(self, name):
            for category in self.data.values():
                  for robot in category:
                        if robot["name"].lower() == name.lower():
                              return robot
            return None


robotz = Her(json_file)
api_token = "8025828818:AAFhIiLB4EJ5WW8I2OtOtStFZKPGVqogoPo"

bot = Bot(token=api_token)
dp = Dispatcher()
router = Router()
dp.include_router(router)

robot_button = InlineKeyboardButton(text="Robot Button", callback_data="robot_list_button")
ethics_button = InlineKeyboardButton(text="Robot Ethics", callback_data="ethics_robot")
keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[[robot_button, ethics_button]])

atlas_button = InlineKeyboardButton(text="Atlas Robot", callback_data="atlas_button")
figure02_button = InlineKeyboardButton(text="Figure 02", callback_data="figure_button")
pepper_button = InlineKeyboardButton(text="Pepper", callback_data="pepper_button")
asimo_button = InlineKeyboardButton(text="Asimo", callback_data="asimo_button")
robonaut2_button = InlineKeyboardButton(text="Robonaut 2", callback_data="robonaut_button")

robots_inline = InlineKeyboardMarkup(inline_keyboard=[[atlas_button, figure02_button, pepper_button, asimo_button, robonaut2_button]])


@dp.message(lambda message: message.text in ["/start", "/help"])
async def start_command(message: types.Message):
      await message.answer("Hello! I am Her. How can I help you today?", reply_markup=keyboard_inline)

@router.callback_query(F.data =="robot_list_button")
async def check_button(callback_query: CallbackQuery):
      await callback_query.message.answer("You selected Robot\'s button", reply_markup=robots_inline)
      await callback_query.answer()


@router.callback_query(F.data =="ethics_robot")
async def check_button(callback_query: CallbackQuery):
      await callback_query.message.answer("You selected Robot\'s Ethics button")
      await callback_query.answer()


@dp.message()
async def get_robot_info(message: types.Message):
      robot_name = message.text.strip()
      robot = robotz.get_robot(robot_name)

      if robot:
            response = (
            f"🤖 The robot you asked is found: {robot['name']};\n" 
            f"🏢 Robot\'s company: {robot['company']};\n"
            f"📏 Robot\'s speed: {robot['speed']};\n"
            f"📏 Robot\'s weight: {robot['weight']};\n"
            f"🔋 Robot\'s battery capacity: {robot['battery_capacity']};\n"
            f"⏳ Robot\'s average runtime: {robot['average_runtime']};\n"
            f"🎛 Level of freedom: {robot['freedom']};"
      )     
            photo = robot.get("image")

            if photo:
                  await message.answer_photo(photo=photo, caption=response)
            else:
                  await message.anwser(response)

      else:
            response = "Robot not found. Try again!"

      




async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())