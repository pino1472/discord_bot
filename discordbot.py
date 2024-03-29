import discord
from discord.ext import tasks,commands
from os import getenv
import traceback
import asyncio
import getURL
import concurrent.futures

client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='/')

@tasks.loop(seconds=30)
async def loop():
    temp =[]

    channel_id = getenv('DISCORD_BOT_CHANNEL')
    await client.wait_until_ready()

    channel = client.get_channel(int(channel_id)) #発言チャンネルを指定
    
    message = await channel.history(limit=25).flatten()
    for msg in message:
        temp.append(msg.content)

    news_list = getURL.url_picker(*temp) #ニュースを取得

    #ニュースをチャットに送信
    for news in news_list:
        await channel.send(news)

token = getenv('DISCORD_BOT_TOKEN')

loop.start()
client.run(token)
