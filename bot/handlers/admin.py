from telegram import Update
from telegram.ext import CallbackContext
from bot.utils.security import is_admin

async def handle_admin_commands(update: Update, context: CallbackContext.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("/kick") and is_admin(update.message.from_user.id):
        await update.message.reply_text("执行踢人命令")
        return True
    return False
