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

### Mitsubishi_api.py
- エアコンなどの赤外線で操作される家電をWEB APIで操作できるようにするための何か。
- irmagicianでの利用を想定している

- 準備
```
sudo apt-get install python-flask python-serial
```

- 起動の仕方
下記のように実行するとHTTPで待ち受ける
```
python Mitsubishi_api.py
```

- つかいかた
下記のようにすると「暖房、設定温度：２１℃、風量：２、風向：水平より１段階下向き」でエアコンを稼働させる信号をirmagician経由で送信する
```
curl "http://localhost:3000/msz_gv2216?mode=warm&temperature=20&wind=2&louver=1"
```

- ファイル
	- Mitsubishi.py
		- 三菱の家電を操作する赤外線信号を生成する
			- エアコン
				- MSZ_GV2216
	- Mitsubishi_api.py
		- Mitsubishi.pyで生成された赤外線信号を実際にirmagician経由で送信するためのAPIを提供する
