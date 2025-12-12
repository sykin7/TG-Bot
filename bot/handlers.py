from telegram import Update
from telegram.ext import CallbackContext
from bot.ai_chat import gpt_reply
from bot.ai_voice import transcribe_voice
from bot.ai_image import generate_image
from bot.admin import check_admin, handle_admin_commands
import os

async def handle_message(update: Update, context: CallbackContext.DEFAULT_TYPE):
    text = update.message.text
    if await handle_admin_commands(update, context):
        return
    if text.startswith("/img"):
        prompt = text.replace("/img", "").strip()
        result = await generate_image(prompt)
        await update.message.reply_photo(result)
    else:
        reply = await gpt_reply(text)
        await update.message.reply_text(reply)

async def handle_voice(update: Update, context: CallbackContext.DEFAULT_TYPE):
    file = await update.message.voice.get_file()
    path = f"temp/{file.file_unique_id}.ogg"
    await file.download_to_drive(path)
    text = await transcribe_voice(path)
    reply = await gpt_reply(text)
    await update.message.reply_text(reply)
    os.remove(path)

async def handle_file(update: Update, context: CallbackContext.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    path = f"downloads/{update.message.document.file_name}"
    await file.download_to_drive(path)
    await update.message.reply_text(f"文件已保存: {path}")
