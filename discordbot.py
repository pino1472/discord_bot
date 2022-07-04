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
NEWS_CHANNEL_ID = 0
tempID = 861810568733392939

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
            return
    # /setupで発言チャンネルをセット
    if message.content == '/setup':
        NEWS_CHANNEL_ID = message.channel.id
        await message.channel.send('チャンネルIDをセット' + str(message.channel.id))
    if message.content == '/reset':
        NEWS_CHANNEL_ID = 0
        await message.channel.send('リセットしました。')

@tasks.loop(seconds=10)
async def loop():
    await client.wait_until_ready()

    if NEWS_CHANNEL_ID == 0:
        return
    channel = client.get_channel(NEWS_CHANNEL_ID) #発言チャンネルを指定

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