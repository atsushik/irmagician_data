# irmagician_data

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