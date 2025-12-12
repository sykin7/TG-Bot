from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

scheduler = AsyncIOScheduler()

def start_scheduler(app):
    async def daily_reminder():
        for chat_id in [123456789]:
            await app.bot.send_message(chat_id=chat_id, text="每日提醒")
    scheduler.add_job(lambda: asyncio.create_task(daily_reminder()), "cron", hour=9)
    scheduler.start()
