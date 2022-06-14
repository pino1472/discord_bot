import discord
from discord.ext import tasks,commands
from os import getenv
import traceback
import asyncio
import RSS
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

@tasks.loop(seconds=10)
async def loop():
    
    channel = client.get_channel(NEWS_CHANNEL_ID) #発言チャンネルを指定
    news_list = rss_picker() #ニュースを取得

    #ニュースをチャットに送信
    for news in news_list:
        await channel.send(news)

@loop.before_loop
async def before_loop():
    # 起動したらログイン通知が表示される
    channel = client.get_channel(tempID) #発言チャンネルを指定
    print(NEWS_CHANNEL_ID)
    await channel.send('開始しました。' + str(NEWS_CHANNEL_ID))

token = getenv('DISCORD_BOT_TOKEN')

loop.start()
client.run(token)