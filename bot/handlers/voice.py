from telegram import Update
from telegram.ext import CallbackContext
from bot.ai.voice import transcribe_voice
from bot.ai.chat import gpt_reply
import os

async def handle_voice(update: Update, context: CallbackContext.DEFAULT_TYPE):
    file = await update.message.voice.get_file()
    path = f"temp/{file.file_unique_id}.ogg"
    await file.download_to_drive(path)
    text = await transcribe_voice(path)
    reply = await gpt_reply(text)
    await update.message.reply_text(reply)
    os.remove(path)
