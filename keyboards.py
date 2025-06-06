from telegram import ReplyKeyboardMarkup

ADMIN_KEYBOARD = ReplyKeyboardMarkup(
    [["کیوبدرادمین"]],
    resize_keyboard=True,
    is_persistent=True  # پارامتر اصلاح شده
)

STAFF_KEYBOARD = ReplyKeyboardMarkup(
    [["کیوبرد نیرو"]],
    resize_keyboard=True,
    is_persistent=True  # پارامتر اصلاح شده
)