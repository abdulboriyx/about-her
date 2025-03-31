from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .intelligence_handler import IntelligenceCallBack

inteldef_button = InlineKeyboardButton(
    text="Intelligence Definition", callback_data=IntelligenceCallBack(intelligence_name="Intelligence Definition").pack()
)
spearman_button = InlineKeyboardButton(
      text="Spearman's General Intelligence",
      callback_data=IntelligenceCallBack(intelligence_name="Spearman's General Intelligence").pack()
)
thrustone_button = InlineKeyboardButton(
      text="Thurstone's Primary Mental Abilities",
      callback_data=IntelligenceCallBack(intelligence_name="Thrustone's Primary Mental Abilities").pack()
)
gardner_button = InlineKeyboardButton(
      text="Garnder's Multiple Intelligences",
      callback_data=IntelligenceCallBack(intelligence_name="Gardner's Multiple Intelligences").pack()
)
sternberg_button = InlineKeyboardButton(
      text="Sternberg's Triarchic Theory",
      callback_data=IntelligenceCallBack(intelligence_name="Sternberg's Triarchic Theory").pack()
)
chc_theory = InlineKeyboardButton(
      text="Cattell-Horn-Carroll (CHC) Theory",
      callback_data=IntelligenceCallBack(intelligence_name="Cattell-Horn-Carroll (CHC) Theory").pack()
)
goleman_button = InlineKeyboardButton(
      text="Goleman's Emotional Intelligence",
      callback_data=IntelligenceCallBack(intelligence_name="Goleman's Emotional Intelligence").pack()
)

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
