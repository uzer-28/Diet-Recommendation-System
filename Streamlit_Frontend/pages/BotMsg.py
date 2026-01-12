import asyncio
from telegram import Bot

# Replace with your bot token and chat ID

class TelegramBot:
    # '7583254091:AAE4rkEJAPZEquWvjlEtEfA4cgQzlMJQVak'
    # '1936587709'
    def __init__(self):
        self.bot = Bot(token='7583254091:AAE4rkEJAPZEquWvjlEtEfA4cgQzlMJQVak')
        self.chat_id = 1936587709

    async def send_message(self, text):
        await self.bot.send_message(chat_id=self.chat_id, text=text)

    def run(self, text):
        asyncio.run(self.send_message(text))