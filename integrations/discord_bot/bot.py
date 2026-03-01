import logging
import os

import discord
from dotenv import load_dotenv

from memu import MemuClient

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
MEMU_API_KEY = os.getenv("MEMU_API_KEY")

if not DISCORD_TOKEN:
    raise SystemExit

if not MEMU_API_KEY:
    raise SystemExit

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
memu = MemuClient(api_key=MEMU_API_KEY)


@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user} (id: {client.user.id})")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    # 将收到的消息保存到 memU 内存中
    conversation = [{"role": "user", "content": message.content}]

    try:
        memu.memorize_conversation(conversation=conversation, user_name=str(message.author), agent_name="discord-bot")
    except Exception:
        logging.exception("Failed to call memu.memorize_conversation")

    # 简单回执 — 可替换为对 memU Response API 的请求以获得智能回复
    try:
        await message.channel.send("消息已保存到 memU 内存。")
    except Exception:
        logging.exception("Failed to send reply")


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
