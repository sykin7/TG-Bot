from telegram import Update
from telegram.ext import CallbackContext

async def start_command(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("TG Bot 已启动，功能齐全！")
