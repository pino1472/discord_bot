from bs4 import BeautifulSoup
import urllib.request as urreq

def url_picker():

    #受け渡しニュースデータ用
    news_list = []

    #1---URL指定
    url = "https://jp.finalfantasyxiv.com/lodestone/topics/"
    ans = urreq.urlopen(url)
    #2---パーサー指定
    soup = BeautifulSoup(ans,'html.parser')
    #3---h2の抽出
    pick_all = soup.select('p.news__list--title')

    for entry in pick_all:
        #前回の最新ニュースに当たれば処理終了 (それ以降は古いニュースの為)
       #if old_news_url == entry.link:
           #break
       #else:
           #ニュースが無いデータを格納
           news_list.append(entry)
    return news_list