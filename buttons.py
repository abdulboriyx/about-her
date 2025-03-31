from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers import RobotCallback, IntelligenceCallBack

# Each Robot's Buttons
atlas_button = InlineKeyboardButton(text="Atlas Robot", callback_data=RobotCallback(robot_name="Atlas").pack())
figure02_button = InlineKeyboardButton(text="Figure 02", callback_data=RobotCallback(robot_name="Figure 02").pack())
pepper_button = InlineKeyboardButton(text="Pepper", callback_data=RobotCallback(robot_name="Pepper").pack())
asimo_button = InlineKeyboardButton(text="ASIMO", callback_data=RobotCallback(robot_name="ASIMO").pack())
robonaut2_button = InlineKeyboardButton(text="Robonaut 2", callback_data=RobotCallback(robot_name="Robonaut 2").pack())
ameca_button = InlineKeyboardButton(text="Ameca", callback_data=RobotCallback(robot_name="Ameca").pack())
apollo_button = InlineKeyboardButton(text="Apollo", callback_data=RobotCallback(robot_name="Apollo").pack())
nao_button = InlineKeyboardButton(text="NAO", callback_data=RobotCallback(robot_name="NAO").pack())
robothespian_button = InlineKeyboardButton(text="RobotheSpian", callback_data=RobotCallback(robot_name="RobotheSpian").pack())


# Intelligent Theories Buttons
inteldef_button = InlineKeyboardButton(text="Intelligence Definition", callback_data=IntelligenceCallBack(intelligence_name="Intelligence Definition").pack())
spearman_button = InlineKeyboardButton(text="Spearman's General Intelligence", callback_data=IntelligenceCallBack(intelligence_name="Spearman's General Intelligence").pack())
thrustone_button = InlineKeyboardButton(text="Thurstone's Primary Mental Abilities", callback_data=IntelligenceCallBack(intelligence_name="Thrustone's Primary Mental Abilities").pack())
gardner_button = InlineKeyboardButton(text="Garnder's Multiple Intelligences", callback_data=IntelligenceCallBack(intelligence_name="Gardner's Multiple Intelligences").pack())
sternberg_button = InlineKeyboardButton(text="Sternberg's Triarchic Theory", callback_data=IntelligenceCallBack(intelligence_name="Sternberg's Triarchic Theory").pack())
chc_theory = InlineKeyboardButton(text="Cattell-Horn-Carroll (CHC) Theory", callback_data=IntelligenceCallBack(intelligence_name="Cattell-Horn-Carroll (CHC) Theory").pack())
goleman_button = InlineKeyboardButton(text="Goleman's Emotional Intelligence", callback_data=IntelligenceCallBack(intelligence_name="Goleman's Emotional Intelligence").pack())


# Robot's Inline Keyboard
robots_inline = InlineKeyboardMarkup(inline_keyboard=[
    [atlas_button, figure02_button],  # Row 1
    [pepper_button, asimo_button],  # Row 2
    [robonaut2_button, ameca_button],  # Row 3
    [apollo_button, nao_button],  # Row 4
    [robothespian_button]  # Row 5
])

# Intelligence theories' inline keyboard
intelligence_inline = InlineKeyboardMarkup(
    inline_keyboard=[
          [inteldef_button],
          [spearman_button],
          [thrustone_button],
          [gardner_button],
          [sternberg_button],
          [chc_theory],
          [goleman_button]
          ]
)
