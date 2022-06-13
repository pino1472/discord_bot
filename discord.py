import discord
from discord.ext import commands
from os import getenv
import traceback
import asyncio
import RSS
import concurrent.futures

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # /setupで発言チャンネルをセット
    if message.content == '/setup':
        NEWS_CHANNEL_ID = message.channel

bot = commands.Bot(command_prefix='/')
client = discord.Client()
@tasks.loop(seconds=60)
async def loop():
    
        channel = client.get_channel(NEWS_CHANNEL_ID) #発言チャンネルを指定
        news_list = rss_picker() #ニュースを取得

        #ニュースをチャットに送信
        for news in news_list:
            await channel.send(news)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)