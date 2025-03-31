from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .button_handlers import RobotCallback

# Define buttons for each robot
atlas_button = InlineKeyboardButton(text="Atlas Robot", callback_data=RobotCallback(robot_name="Atlas").pack())
figure02_button = InlineKeyboardButton(text="Figure 02", callback_data=RobotCallback(robot_name="Figure 02").pack())
pepper_button = InlineKeyboardButton(text="Pepper", callback_data=RobotCallback(robot_name="Pepper").pack())
asimo_button = InlineKeyboardButton(text="ASIMO", callback_data=RobotCallback(robot_name="ASIMO").pack())
robonaut2_button = InlineKeyboardButton(text="Robonaut 2", callback_data=RobotCallback(robot_name="Robonaut 2").pack())
ameca_button = InlineKeyboardButton(text="Ameca", callback_data=RobotCallback(robot_name="Ameca").pack())
apollo_button = InlineKeyboardButton(text="Apollo", callback_data=RobotCallback(robot_name="Apollo").pack())
nao_button = InlineKeyboardButton(text="NAO", callback_data=RobotCallback(robot_name="NAO").pack())
robothespian_button = InlineKeyboardButton(text="RobotheSpian", callback_data=RobotCallback(robot_name="RobotheSpian").pack())

# Organize buttons into an inline keyboard
robots_inline = InlineKeyboardMarkup(inline_keyboard=[
    [atlas_button, figure02_button],  # Row 1
    [pepper_button, asimo_button],  # Row 2
    [robonaut2_button, ameca_button],  # Row 3
    [apollo_button, nao_button],  # Row 4
    [robothespian_button]  # Row 5
])
