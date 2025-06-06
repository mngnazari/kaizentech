from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, Update, InlineKeyboardMarkup, InlineKeyboardButton # InlineKeyboard ها اضافه شدند
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler # CallbackQueryHandler اضافه شد

# ایمپورت STAFFS از فایل config
from config import STAFFS #

# توابع placeholder برای admin_command و cube_admin
async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("شما وارد بخش مدیریت شدید!")

async def cube_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("منوی کیوب ادمین در حال آماده‌سازی است...")

# تابع جدید برای مدیریت انتخاب نیرو از کیبورد شیشه‌ای
async def select_staff_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # ضروری برای جلوگیری از حالت لودینگ روی دکمه

    callback_data = query.data

    if callback_data.startswith("select_staff_"):
        staff_id_str = callback_data.replace("select_staff_", "")
        try:
            selected_staff_id = int(staff_id_str)
            staff = next((s for s in STAFFS if s["id"] == selected_staff_id), None) #

            if staff:
                response = (
                    f"👤 شما نیرو {staff['name']} را انتخاب کردید.\n"
                    f"🆔 آیدی: `{staff['id']}`\n\n"
                    "لطفا عملیات مورد نظر را انتخاب کنید:"
                )

                # ایجاد کیبورد عملیات برای نیروی انتخاب شده
                actions_keyboard = ReplyKeyboardMarkup( # همچنان می توانید از ReplyKeyboardMarkup برای منوهای بعدی استفاده کنید
                    [
                        ["ویرایش اطلاعات", "حذف نیرو"],
                        ["مشاهده گزارشات", "بازگشت"]
                    ],
                    resize_keyboard=True,
                    is_persistent=True
                )

                await query.edit_message_text( # استفاده از edit_message_text برای ویرایش پیام قبلی
                    response,
                    reply_markup=actions_keyboard,
                    parse_mode="Markdown"
                )
            else:
                await query.edit_message_text("⚠️ نیرو انتخاب شده نامعتبر است.")

        except ValueError:
            await query.edit_message_text("⚠️ خطایی در شناسایی آیدی نیرو رخ داد.")
    elif callback_data == "manage_staffs":
        await query.edit_message_text(
            "منوی مدیریت نیروها در حال آماده‌سازی است...",
            reply_markup=ReplyKeyboardRemove()
        )


# به روزرسانی هندلرها
ADMIN_HANDLERS = [
    CommandHandler("admin", admin_command),
    MessageHandler(filters.Regex(r"^کیوبدرادمین$"), cube_admin),
    # هندلر قبلی برای ReplyKeyboardMarkup بود، اکنون از CallbackQueryHandler استفاده می‌کنیم
    CallbackQueryHandler(select_staff_callback, pattern=r"^(select_staff_|manage_staffs)$") # CallbackQueryHandler اضافه شد
]