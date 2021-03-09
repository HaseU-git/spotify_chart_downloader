# spotify_chart_downloader

## 概要
このコードは、[こちら](https://spotifycharts.com/regional)のランキングデータを複数日分一気にダウンロードするために作成したプログラムです。  

サイトからもcsvをダウンロードする機能はついていますが、複数日を指定してダウンロードする機能はなく、ページを行き来する必要があるため、これらの手間を削減するために作ったものです。  

`project`ディレクトリの中にコードと、コードを動かすために必要なファイル、フォルダーが入っています。  

<hr>

- spotify_chart_scraping.py
`spotifycharts.com`からデータを取得しcsvに書き出すためのコードです。  

- date.csv
取得したい日にちをこのcsvファイルの中に書き込みます。  

- datas
このフォルダの中に書き出したcsvファイルが保存されます。  

<hr>

## 目的
pythonを使用した初めてのコードで、pythonのコードの書き方やpipの使い方などを取得することが主な目的でした。  
また、HTML、CSSを習得したばかりの頃に書いたコードなので、学んだ知識を生かしてみるという目的もありました。  

## 使い方
まず、リポジトリをクローンします。  

```shell
git clone https://github.com/HaseU-git/spotify_chart_downloader
cd spotify_chart_downloader/project
```

`pip`を利用して必要なライブラリをインストールします。  

```shell
pip install requests
pip install Beatifulsoup4
```

次に、自分が必要としている日付を`date.csv`に記述します。  
ここでは、2017年から2021年までの各年の元旦の情報をを記述します。  

```shell
echo "2017-01-01,2018-01-01,2019-01-01,2020-01-01,2021-01-01" > date.csv
```

日本以外の情報を取得したい場合には、`spotify_chart_scraping.py`のコードの`COUNTRY`の部分を自分が取得したい国に書き換えてください。  

最後にプログラムを実行します。  
取得した情報は、日にちごとにcsvに出力され`datas`ディレクトリに保存されます。  

```shell
python3 spotify_chart_scraping.py
```

## 開発環境
- MacBook Pro (15-inch, 2018)
- macOS Big Sur Version 11.2.1
- python 3.9.1
- beautifulsoup4 4.9.3
- requests 2.25.1
