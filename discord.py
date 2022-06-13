from discord.ext import tasks,commands
from os import getenv
import traceback
import asyncio
import RSS
import concurrent.futures

bot = commands.Bot(command_prefix='/')

@looper.before_loop
async def on_ready():
    # �N��������^�[�~�i���Ƀ��O�C���ʒm���\�������
    print('�J�n���܂��B')

# ���b�Z�[�W��M���ɓ��삷�鏈��
@bot.command()
async def setup(message):
    # ���b�Z�[�W���M�҂�Bot�������ꍇ�͖�������
    if message.author.bot:
        return
    # /setup�Ŕ����`�����l�����Z�b�g
    NEWS_CHANNEL_ID = message.channel
    self.looper.start()

@tasks.loop(seconds=60)
async def looper():
    
        channel = client.get_channel(NEWS_CHANNEL_ID) #�����`�����l�����w��
        news_list = rss_picker() #�j���[�X���擾

        #�j���[�X���`���b�g�ɑ��M
        for news in news_list:
            await channel.send(news)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)