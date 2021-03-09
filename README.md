# spotify_chart_downloader

## 概要
このコードは、[こちら](https://spotifycharts.com/regional)のランキングデータを複数日分一気にダウンロードするために作成したプログラムです。  


## 目的

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

日本以外の情報を取得したい場合には、`spootify_chart_downloader.py`のコードの`COUNTRY`の部分を自分が取得したい国に書き換えてください。  

最後にプログラムを実行します。  
取得した情報は、日にちごとにcsvに出力され`datas`ディレクトリに保存されます。  

```shell
python3 spotify_chart_downloader.py
```

## 開発環境
