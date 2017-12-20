# これはなに？
[irmagician](http://www.omiya-giken.com/?page_id=837)で使うためのリモコン信号データと、それらを生成するためのスクリプト。
# どう使えるの？
[irmagician](http://www.omiya-giken.com/?page_id=837)　を コマンドラインから使うためのスクリプト[irmcli](https://github.com/atsushik/irmcli)への入力として使う。
## データ
↓のように配置されているから、適当なファイル名を[irmcli](https://github.com/atsushik/irmcli)コマンドの-fに指定する
```
./メーカー名/製品名/リモコン信号データ.json
```
## スクリプト
### mitsubishi_msz-gv2216.py
三菱のエアコン用のリモコン信号を生成する
- mode
  - 機能を指定する

<<<<<<< HEAD
for use with https://github.com/netbuffalo/irmcli.git

## this is なに？
- エアコンなどの赤外線で操作される家電をWEB APIで操作できるようにするための何か。
- irmagicianでの利用を想定している

## 起動の仕方
下記のように実行するとHTTPで待ち受ける
```
python Mitsubishi_api.py
```

## つかいかた
下記のようにすると「暖房、設定温度：２１℃、風量：２、風向：水平より１段階下向き」でエアコンを稼働させる信号をirmagician経由で送信する
```
curl "http://localhost:3000/msz_gv2216?warm=21&temperature=23&wind=2&louver=1"
```

## ファイル
- Mitsubishi.py
	- 三菱の家電を操作する赤外線信号を生成する
		- エアコン
			- MSZ_GV2216
- Mitsubishi_api.py
	- Mitsubishi.pyで生成された赤外線信号を実際にirmagician経由で送信するためのAPIを提供する
=======
|説明|値|
|:---:|:---:|
|cool|冷房|
|dehumidify|除湿|
|warm|暖房|
|off|オフ|

- temperature
  - 設定温度を指定する

- wind
  - 風量を指定する

|説明|値|
|:---:|:---:|
|Auto|自動|
|1〜3|弱〜強|

- louver
  - 風向きを指定する

|説明|値|
|:---:|:---:|
|Auto|自動|
|All|巡回|
|0〜4|前方〜真下|

- 使用例1
  - [三菱のルームエアコン(霧ヶ峰) MSZ-GV2216-W](https://www.mitsubishielectric.co.jp/ldg/wink/displayProduct.do?pid=262783&c040101410)に対して、下記の信号を送りたいときの例

|オプション名|説明|値|
|:---:|:---:|:---:|
|mode|モード|暖房|
|temperature|設定温度|23℃|
|wind|風量|2|
|louver|風向|1(真横が0〜真下が4)|

```
python ~/git/irmagician_data/mitsubishi_msz-gv2216.py --mode warm --temperature 22 --wind 2 --louver 1 | python ~/git/irmcli/irmcli.py -p -f -
```
>>>>>>> 8f30ba744fd7f7315f8c521c1c899c2bba0bc269
