import discord
from discord.ext import commands
from os import getenv
import traceback
import asyncio
import RSS
import concurrent.futures

@client.event
async def on_ready():
    # �N��������^�[�~�i���Ƀ��O�C���ʒm���\�������
    print('���O�C�����܂���')

# ���b�Z�[�W��M���ɓ��삷�鏈��
@client.event
async def on_message(message):
    # ���b�Z�[�W���M�҂�Bot�������ꍇ�͖�������
    if message.author.bot:
        return
    # /setup�Ŕ����`�����l�����Z�b�g
    if message.content == '/setup':
        NEWS_CHANNEL_ID = message.channel

bot = commands.Bot(command_prefix='/')
client = discord.Client()
@tasks.loop(seconds=60)
async def loop():
    
        channel = client.get_channel(NEWS_CHANNEL_ID) #�����`�����l�����w��
        news_list = rss_picker() #�j���[�X���擾

        #�j���[�X���`���b�g�ɑ��M
        for news in news_list:
            await channel.send(news)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)