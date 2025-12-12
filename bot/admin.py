import os
from telegram import Update
from telegram.ext import CallbackContext

ADMIN_ID = int(os.environ.get("ADMIN_ID", 0))

async def check_admin(user_id):
    return user_id == ADMIN_ID

async def handle_admin_commands(update: Update, context: CallbackContext.DEFAULT_TYPE):
    text = update.message.text
    if text.startswith("/kick") and await check_admin(update.message.from_user.id):
        await update.message.reply_text("执行踢人命令")
        return True
    return False
