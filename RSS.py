import feedparser
import git

# urlは適宜自身が編集可能なレポジトリに書き換えてください
url = 'https://github.com/pino1472/discord_bot.git'

# cloneしたプロジェクトを出力するパス
to_path = 'data'
log_path = 'data/log.txt' #logファイルのパス

RSS_URL = 'https://www.happyou.info/fs/gen.php?u=-1032701763&p=139401332' #AUTOMATONのRSS-URL

def rss_picker():
    #受け渡しニュースデータ用
    news_list = []

    git.Repo.clone_from(
    url,
    to_path)

    #logから前回取得した最新のニュースURLを取得
    with open(log_path, mode='r') as f:
        old_news_url = f.read()
        print('前回取得したニュースURL: '+ old_news_url)

    #最新のニュースを取得
    d = feedparser.parse(RSS_URL)
    for entry in d.entries:

       #前回の最新ニュースに当たれば処理終了 (それ以降は古いニュースの為)
       if old_news_url == entry.link:
           break
       else:
           #ニュースが無いデータを格納
           news_list.append(entry.link)
    #前回の最新ニュースが先頭ではない場合
    if old_news_url != d.entries[0].link:
           #最新のニュースURLに置き換える
           try:
               with open(log_path, mode='w') as f:
                   f.write(d.entries[0].link)

               repo.git.add('log.txt')
               repo.git.commit('log.txt', message='update', author='pino1472')
               repo.git.push('origin', 'main')
               repo.git.push('--delete', 'origin', 'main')
           except IndexError:
               print('正常にニュースを取得できませんでした。')
               print('次のサイトのRSSフィード等を再度確認してください: '+ site_name)
    return news_list