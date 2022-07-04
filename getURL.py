from bs4 import BeautifulSoup
import urllib.request as urreq
import re

def url_picker(*last_msg):

    news_list = []

    url = "https://jp.finalfantasyxiv.com/lodestone/topics/"
    ans = urreq.urlopen(url)

    soup = BeautifulSoup(ans,'html.parser')

    pick_all = soup.select('p.news__list--title')

    news_diff = pick_all - last_msg

    for entry in news_diff:

        entry.replace('<p class="news__list--title"><a href="','').replace('">','').replace('</a></p>','')
        entryReg = re.split('(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)',entry)
        entryReg[1] = '**' + entryReg[1] +'**'
        entry = entryReg[1] + '\n' + entryReg[0]
        news_list.append(entry)
    return news_list
