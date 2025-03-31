from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData
from .robotz import get_robot


router = Router()

# Unified CallbackData for all robots
class RobotCallback(CallbackData, prefix="robot"):
    robot_name: str



async def send_robot_info(callback_query: CallbackQuery, robot_name: str):
    robot = get_robot(robot_name)



    if robot:
        response = (
            f"🤖 The robot you asked is found: {robot['name']}\n"
            f"🏢 Robot's company: {robot['company']}\n"
            f"📏 Robot's speed: {robot['speed']}\n"
            f"📏 Robot's weight: {robot['weight']}\n"
            f"🔋 Robot's battery capacity: {robot['battery_capacity']}\n"
            f"⏳ Robot's average runtime: {robot['average_runtime']}\n"
            f"🎛 Level of freedom: {robot['freedom']}\n"
            f"🔗 More information: {robot['link']}\n\n"
            f"{robot['special']}\n\n@herrobotics_bot"
        )
        photo = robot.get("image")

        if photo:
            await callback_query.message.answer_photo(photo=photo, caption=response)
        else:
            await callback_query.message.answer(response)
    else:
        response = "Robot not found. Try again!"
        await callback_query.message.answer(response)


# Register callback query handlers for each robot
@router.callback_query(RobotCallback.filter())
async def handle_robot_callback(callback_query: CallbackQuery, callback_data: RobotCallback):
    await send_robot_info(callback_query, callback_data.robot_name)


