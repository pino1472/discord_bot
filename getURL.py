from bs4 import BeautifulSoup
import urllib.request as urreq

def url_picker():

    #�󂯓n���j���[�X�f�[�^�p
    news_list = []

    #1---URL�w��
    url = "https://jp.finalfantasyxiv.com/lodestone/topics/"
    ans = urreq.urlopen(url)
    #2---�p�[�T�[�w��
    soup = BeautifulSoup(ans,'html.parser')
    #3---h2�̒��o
    pick_all = soup.select('p.news__list--title')

    for entry in pick_all:
        #�O��̍ŐV�j���[�X�ɓ�����Ώ����I�� (����ȍ~�͌Â��j���[�X�̈�)
       #if old_news_url == entry.link:
           #break
       #else:
           #�j���[�X�������f�[�^���i�[
           news_list.append(entry)
    return news_list