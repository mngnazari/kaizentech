from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دستور ادمین اجرا شد")

async def cube_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("عملیات مخصوص ادمین اجرا شد")

ADMIN_HANDLERS = [
    CommandHandler("admin", admin_command),
    MessageHandler(filters.Regex(r"^کیوبدرادمین$"), cube_admin)
]