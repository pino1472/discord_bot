from bs4 import BeautifulSoup
import urllib.request as urreq
import re

def url_picker(*last_msg):

    news_list = []

    url = "https://jp.finalfantasyxiv.com/lodestone/topics/"
    ans = urreq.urlopen(url)

    soup = BeautifulSoup(ans,'html.parser')

    pick_all = soup.select('p.news__list--title')

    for entry in pick_all:
        temp = str(entry).replace('<p class="news__list--title"><a href="','').replace('">',' ').replace('</a></p>','')
        tempSplit = str(temp).split(' ',1)
        temps = '**' + str(tempSplit[1]) +'**'
        entrys = temps + '\n' + 'https://jp.finalfantasyxiv.com' + str(tempSplit[0])
        news_list.append(entrys)

    news_diff = list(set(news_list) - set(last_msg))

    return news_diff
