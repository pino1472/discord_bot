import discord
import asyncio
import RSS
import concurrent.futures

TOKEN = 'ODkzMTc3MjgyMDQxMDg2MDIy.YVXqKg.oBD9_HJvQRJ89Gzb-j3jG957WLA'
client = discord.Client()
@tasks.loop(seconds=60)
async def loop():
    
        channel = client.get_channel(NEWS_CHANNEL_ID) #発言チャンネルを指定
        news_list = rss_picker() #ニュースを取得

        #ニュースをチャットに送信
        for news in news_list:
            await channel.send(news)