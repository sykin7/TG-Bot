from telegram import Update
from telegram.ext import CallbackContext
from bot.ai.chat import gpt_reply
from bot.handlers.admin import handle_admin_commands
from bot.ai.image import generate_image

async def handle_message(update: Update, context: CallbackContext.DEFAULT_TYPE):
    text = update.message.text
    if await handle_admin_commands(update, context):
        return
    if text.startswith("/img"):
        prompt = text.replace("/img", "").strip()
        url = await generate_image(prompt)
        await update.message.reply_photo(url)
    else:
        reply = await gpt_reply(text)
        await update.message.reply_text(reply)
