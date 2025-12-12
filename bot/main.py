import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.commands.start import start_command
from bot.handlers.message import handle_message
from bot.handlers.voice import handle_voice
from bot.handlers.file import handle_file
from bot.scheduler.tasks import start_scheduler
from dotenv import load_dotenv

load_dotenv('../config/config.env')
BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(MessageHandler(filters.VOICE, handle_voice))
app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

start_scheduler(app)
app.run_polling()
