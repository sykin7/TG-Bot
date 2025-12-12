from telegram import Update
from telegram.ext import CallbackContext
from bot.utils.security import is_safe_file
import os

async def handle_file(update: Update, context: CallbackContext.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    if not is_safe_file(update.message.document.file_name):
        await update.message.reply_text("不允许的文件类型")
        return
    path = f"downloads/{update.message.document.file_name}"
    await file.download_to_drive(path)
    await update.message.reply_text(f"文件已保存: {path}")
