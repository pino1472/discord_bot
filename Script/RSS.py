RSS_URL = 'https://www.happyou.info/fs/gen.php?u=-1032701763&p=139401332' #AUTOMATONのRSS-URL

log_path = 'data/log.txt' #logファイルのパス

no_news_flg = 1 #最新ニュース有無のフラグ

#受け渡しニュースデータ用
news_list = []

#logから前回取得した最新のニュースURLを取得
with open(log_path, mode='r') as f:
    old_news_url = f.read()
    print('前回取得したニュースURL: '+ old_news_url)

#最新のニュースを取得
d = feedparser.parse(RSS_URL)
for entry in d.entries:

    #前回の最新ニュースに当たれば処理終了 (それ以降は古いニュースの為)
    if old_news_url == entry.link:
        print('最新のニュースは以上です')
        break

if no_news_flg == 0:
    #最新のニュースURLに置き換える
    with open(log_path, mode='w') as f:
        f.write(d.entries[0].link)

else:
    #ニュースが無いデータを格納
    news_list.append('最新のゲーム無料配布ニュースはありません')