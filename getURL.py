from bs4 import BeautifulSoup
import urllib.request as urreq

def url_picker(*last_msg):

    #�󂯓n���j���[�X�f�[�^�p
    news_list = []

    #1---URL�w��
    url = "https://jp.finalfantasyxiv.com/lodestone/topics/"
    ans = urreq.urlopen(url)
    #2---�p�[�T�[�w��
    soup = BeautifulSoup(ans,'html.parser')
    #3---h2�̒��o
    pick_all = soup.select('p.news__list--title')

    news_diff = pick_all - last_msg

    for entry in news_diff:
        #�j���[�X�������f�[�^���i�[
        news_list.append(entry)
    return news_list