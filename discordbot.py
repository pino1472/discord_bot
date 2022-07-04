import discord
from discord.ext import tasks,commands
from os import getenv
import traceback
import asyncio
import RSS
import getURL
import concurrent.futures

client = discord.Client()
bot = commands.Bot(command_prefix='/')

@tasks.loop(seconds=10)
async def loop():
    channel_id = getenv('DISCORD_BOT_CHANNEL')
    await client.wait_until_ready()

    channel = client.get_channel(channel_id) #発言チャンネルを指定

    last_msg = []
    # 取得したチャンネルの最後のメッセージを取得する
    async for msg in channel.history(limit=20):
        last_msg.append(msg)

    news_list = getURL.url_picker(*last_msg) #ニュースを取得

    #ニュースをチャットに送信
    for news in news_list:
        await channel.send(news)

token = getenv('DISCORD_BOT_TOKEN')

loop.start()
client.run(token)