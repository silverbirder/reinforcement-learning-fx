# README #

## 準備 ##
    # mongodb
    windows -> https://downloads.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-3.6.0-signed.msi
    mac -> https://downloads.mongodb.org/osx/mongodb-shell-osx-ssl-x86_64-3.6.0.tgz

    pip install mongo
    pip install pymongo
    pip install oandapy
    pip install gym
    pip install pyyaml
    
    上記のpip install で動かないときはこれを試してみて。
    sudo apt install python-pip python3-pip
    sudo pip3 install pyyaml mongo pymongo gym oandapy
    

## 実行 ##
    python auto_order.py

## dockerを使ったauto_orderの起動方法 ##
    git clone https://bitbucket.org/ma-matsuoka/reinforcement-learning-fx.git fxTrade/
    コンフィグファイルの設定をする。
    sh ./deploy.sh
    python3 ~/fxTrade/auto_order.py

## OANDA REST API 動作確認 ##

### 事前準備   
  1. OANDA 無料デモ口座を開設する   
     [OANDA fxTrade Practice](https://www.oanda.jp/service/demo.php)   
  1. `REST APIアクセスの管理`から`Personal Access Token`を発行する   
  1. `config/account.yml`のアカウント情報を編集する   

|セクション      |項目                 |設定値                                                   |
|:-------------|:-------------------|:--------------------------------------------------------|
|oanda         |access_token        |`REST APIアクセスの管理`から発行した`Personal Access Token`  |
|              |account_id          |`口座情報 アカウント`から選択した口座アカウントID               |

### 動作確認   
  1. リアルタイムレートを取得する   
     `python3 tools.py -k fsr`   
  1. 口座情報を確認する   
     `python3 tools.py -k fa`   
  1. 注文を行う   
     `python3 tools.py -k eco`   
  1. 注文一覧を取得する   
     `python3 tools.py -k fol`   
     ※ __Oanda 取引プラットフォーム: Web版 > 取引履歴__ からも確認できます   

## 参考URL ##
[OpenAI GymでFXのトレーディング環境を構築する](https://qiita.com/hide-tono/items/bb9691477831e48f0989)  
[ゼロからDeepまで学ぶ強化学習](https://qiita.com/icoxfog417/items/242439ecd1a477ece312)  
[GitHub: oanda/oandapy](https://github.com/oanda/oandapy)   
[OANDA REST API](http://developer.oanda.com/rest-live/introduction/)

## 参考書籍 ##
[強化学習と深層学習 C言語によるシミュレーション](https://goo.gl/BY3MNq)  
[これからの強化学習](https://goo.gl/kjYHf3)  

## 連絡など ##

- Slackにワークスペースを作成しました。   
  Slackに通知が飛びます。   
   [reinforcement-learning-fx への招待リンク](https://join.slack.com/t/reinforcement-fx/shared_invite/enQtMjg4MjE0NDMyNDM4LTQ0MzZkODA2MGM2NjUzMWRlMTNkNTIzMzFiMWQ5OGE3YTQ1YjkzODg5NWMyOTczMTZmNThlZWRkZmUzMmU3NGI)
