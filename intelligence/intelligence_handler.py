from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData
from .intelligence_theory import get_intelligence

router = Router()

class IntelligenceCallBack(CallbackData, prefix="intelligence"):
    intelligence_name: str

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

@router.callback_query(IntelligenceCallBack.filter())
async def handle_intelligence_callback(callback_query: CallbackQuery, callback_data: IntelligenceCallBack):
    print("handle_intelligence_callback function was called!")  # Add this line
    await send_intelligence_theory(callback_query, callback_data.intelligence_name)
