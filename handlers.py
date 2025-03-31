from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData
from robotlist.robotz import get_robot
from intelligence.intelligence_theory import get_intelligence
from conscious_theory import get_conscious

router = Router()

# Robotics Class CallBackData
class RobotCallback(CallbackData, prefix="robot"):
    robot_name: str

# Intelligence theory's callbackdata
class IntelligenceCallBack(CallbackData, prefix="intelligence"):
    intelligence_name: str

# Consciousness CallbackData
class ConsciousCallBack(CallbackData, prefix="conscious"):
    conscious_thought: str

# robotics function
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


# intelligence function
async def send_intelligence_theory(callback_query: CallbackQuery, intelligence_name: str):
    intelligence = get_intelligence(intelligence_name)

    if intelligence:
        response = (
            f"{intelligence['name']}; {intelligence['theory']}"
        )
        await callback_query.message.answer(response) 
    else:
        response = "No theory found. Try again!"
        await callback_query.message.answer(response)



# conscious func
async def send_conscious_thought(callback_query: CallbackQuery, conscious_thought: str):
    conscious = get_conscious(conscious_thought)

    if conscious:
        response = (
            f"{conscious['name']}; {conscious['theory']}"
        )
        await callback_query.message.answer(response)
    else:
        response = "Not found. Try again!"
        await callback_query.message.answer(response)


@router.callback_query(RobotCallback.filter())
async def handle_robot_callback(callback_query: CallbackQuery, callback_data: RobotCallback):
    await send_robot_info(callback_query, callback_data.robot_name)


@router.callback_query(IntelligenceCallBack.filter())
async def handle_intelligence_callback(callback_query: CallbackQuery, callback_data: IntelligenceCallBack):
    print("handle_intelligence_callback function was called!")  # Add this line
    await send_intelligence_theory(callback_query, callback_data.intelligence_name)

@router.callback_query(ConsciousCallBack.filter())
async def handle_consciousness_callback(callback_query: CallbackQuery, callback_data: ConsciousCallBack):
    await send_conscious_thought(callback_query, callback_data.conscious_thought)