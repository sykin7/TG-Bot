import schedule, asyncio

def start_scheduler(app):
    async def job():
        for chat_id in [123456789]:  # 可以放群ID列表
            await app.bot.send_message(chat_id=chat_id, text="定时提醒消息")
    def run_schedule():
        schedule.every(10).minutes.do(lambda: asyncio.run(job()))
        while True:
            schedule.run_pending()
    import threading
    t = threading.Thread(target=run_schedule)
    t.start()
