from discord.ext import tasks,commands
from os import getenv
import traceback
import asyncio
import RSS
import concurrent.futures

bot = commands.Bot(command_prefix='/')

@looper.before_loop
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('開始します。')

# メッセージ受信時に動作する処理
@bot.command()
async def setup(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # /setupで発言チャンネルをセット
    NEWS_CHANNEL_ID = message.channel
    self.looper.start()

@tasks.loop(seconds=60)
async def looper():
    
        channel = client.get_channel(NEWS_CHANNEL_ID) #発言チャンネルを指定
        news_list = rss_picker() #ニュースを取得

        #ニュースをチャットに送信
        for news in news_list:
            await channel.send(news)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)