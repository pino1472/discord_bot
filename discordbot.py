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

@tasks.loop(seconds=60)
async def loop():
    await client.wait_until_ready()

    channel = client.get_channel(tempID) #発言チャンネルを指定

    
    # 取得したチャンネルの最後のメッセージを取得する
    last_msg = await channel.fetch_message(channel.last_message_id)

    news_list = getURL.url_picker(last_msg) #ニュースを取得

    #ニュースをチャットに送信
    for news in news_list:
        await channel.send(news)

token = getenv('DISCORD_BOT_TOKEN')

loop.start()
client.run(token)