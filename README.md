# spotify_chart_downloader
spotify_chart_downloaderは、

## 背景
大学1年の「データ解析入門」という授業の最終課題のレポートにおいて、私はSpotifyのチャートの「Stream」を目的変数としてデータ解析を行った。  
説明変数にはTwitterのツイート数、Instagramの投稿数、YouTubeの動画の投稿数、各SNSのフォロワー数などを設定した。  
このモデルを作成するにあたり、それぞれの説明変数、及び目的変数の情報をデータとして取得するつようがあった。  
1年の時には、データを収集するにあたりSeleniumというWebアプリケーションのUIテスト自動化ツールを応用し、ブラウザの操作を自動化しターゲットとなる情報を取得するという方法を用いた。  
このようにデータ収集をする際に、プログラムを書くことでデータを収集するという単純作業を効率化できることを学んだ。  
しかしながら、Seleniumをつかったデータ収集には欠点があり、それぞれのローカル環境にOSとブラウザバージョンに対応するWebDriverをインストールするという環境設定が必要になる。  
この点において、Seleniumは気軽に実行できるものであるとは言い難い。  
そこで、別の方法としてBeautiful SoupというHTMLからの情報を簡単に抽出することができるようになるpythonのライブラリを用いいるということが考えられる。  
この方法を使用すれば、環境設定をすることなく情報収集を効率化することができるのではないかと考えた。  
また、それをさらにWebアプリケーションに組み込むことができればデータの収集を誰もが簡単に行えるようになるのではないかと考えた。  
このプロジェクトでは、SpotifyChartのデータをダウンロードすることができるようになることを目的としている。  
対象としてSpotifyChartを選んだ理由としては以下の通りである。  
- Spotifyは世界最大級の音楽ストリーミングサービスであり、チャートのデータは実際の分析にも役立てることができる  
- robots.txtによってクローリングが禁止されていない
- HTMLが整形されており、スクレイピングがしやすい  
- CSVダウンロード機能はあるが、日時を指定して一括ダウンロードでき機能がない
- CSV一括ダウンロード機能のあるサービスが他に存在しない（なさそう）

このようなデータ収集のためのWebアプリケーションの作り方を習得することができれば、今後星野ゼミに入った場合、データを収集する際に役立てることができると思ったのも、このプロジェクトの制作に取り掛かった一つの理由である。  
具体的には、APIを作成しCSVをいちいちダウンロードすることなくデータ解析のためのプログラムに組み込めるようにすれば、ゼミ生の誰もが簡単にデータを扱えるようになり星野ゼミの発展に貢献できるのではないかと考えている。

## 開発環境

## アプリの仕様
日にちが変わったタイミングで以下の処理を行う  
(1時間ごとにやるのでも面白いかも）

1. 未獲得テーブルに入っている日にちの分と新しい日付のデータをスクレイピングしようとする
2. 新しい日付を日付テーブルに追加する
3. スクレイピンに失敗したものを未獲得テーブルに追加する 
↑を地域ごとに全て行う

<hr>

指定画面で指定したものを処理する手順  

1. 未獲得テーブルとかぶっているかを確認する
2. かぶっていた場合には、エラー、かぶっていなかったら次に行く
3. 日付テーブルとかぶっていないものがないか確認する  
4. 日付テーブルにないものがあったらエラー、なかったら次に行く
5. 実際にデータをとってきて、日付ごとにランキングで並び替える
→ エラーならエラーをハく？
6. CSVファイルをつくり、ZIP形式でダウンロードさせる。 





## モデル

### アーティストテーブル
- アーティスト名（char型）

### 日付テーブル
SpotifyChartの一番最初の日にちから今現在までの日付が入っている  
- 日付（date型）

### 曲テーブル
- 曲名（char型)
- アーティスト名（外部キー）

### 地域テーブル
- 地域名

### ランキングテーブル
- 曲名（外部キー）
- 地域名（char型）
- Stream（int型）
- 日付（外部キー）

### 未獲得テーブル
- 日付（外部キー）
- 地域（外部キー） 

## 推移画面

### 指定画面
- 日付（開始日）
- 日付（終了日）
- 地域
を指定する（日付が同じ場合にはその日のみのデータをとってくる）

### チェック画面
エラーコードにおうじてmsgを表示する、または、データの獲得に成功したmsgを表示する画面  
- msg
- 指定画面へのリンク

## 拡張性
アーティストの項目にレーベルなどを追加？  
今日のジャンルについて追加？？  
スクレイピングが完了した時点でline botにメッセージを送るようにする
line botからコマンドを受け取り、出力する


