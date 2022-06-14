from discord.ext import tasks,commands
from os import getenv
import traceback
import asyncio
import RSS
import concurrent.futures

bot = commands.Bot(command_prefix='/')
NEWS_CHANNEL_ID = 0

# メッセージ受信時に動作する処理
@bot.command()
async def setup(ctx):
    # メッセージ送信者がBotだった場合は無視する
    if ctx.author.bot:
            return
    # /setupで発言チャンネルをセット
    NEWS_CHANNEL_ID = ctx.channel.id
    await ctx.send(NEWS_CHANNEL_ID + 'チャンネルIDをセット' + str(ctx.channel.id))

@tasks.loop(seconds=10)
async def loop():
    
    channel = bot.get_channel(NEWS_CHANNEL_ID) #発言チャンネルを指定
    news_list = rss_picker() #ニュースを取得

    #ニュースをチャットに送信
    for news in news_list:
        await channel.send(news)

@loop.before_loop
async def before_loop():
    # 起動したらログイン通知が表示される
    channel = bot.get_channel(NEWS_CHANNEL_ID) #発言チャンネルを指定
    await channel.send('開始しました。')

token = getenv('DISCORD_BOT_TOKEN')

loop.start()
bot.run(token)