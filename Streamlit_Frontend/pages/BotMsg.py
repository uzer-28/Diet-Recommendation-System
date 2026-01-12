import asyncio
from telegram import Bot

# Replace with your bot token and chat ID

class TelegramBot:
    def __init__(self):
        self.bot = Bot(token='')
        self.chat_id = 

    async def send_message(self, text):
        await self.bot.send_message(chat_id=self.chat_id, text=text)

    def run(self, text):

        asyncio.run(self.send_message(text))
