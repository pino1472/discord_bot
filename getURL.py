from bs4 import BeautifulSoup
import urllib.request as urreq
import re

def url_picker(*last_msg):

    news_list = []

    url = "https://jp.finalfantasyxiv.com/lodestone/topics/"
    ans = urreq.urlopen(url)

    soup = BeautifulSoup(ans,'html.parser')

    pick_all = soup.select('p.news__list--title')

    news_diff = list(set(pick_all) - set(last_msg))

    for entry in news_diff:

        str(entry).replace('</a></p>','').replace('">',' ').replace('<p class="news__list--title"><a href="','')
        entryReg = str(entry).split()
        entryRegs = '**' + str(entryReg[1]) +'**'
        entrys = entryRegs + '\n' + str(entryReg[0])
        news_list.append(entrys)
    return news_list
