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
-- 機能を指定する

|説明|値|
|:---:|:---:|
|cool|冷房|
|dehumidify|除湿|
|warm|暖房|
|off|オフ|

- temperature
-- 設定温度を指定する

- wind
-- 風量を指定する

|説明|値|
|:---:|:---:|
|Auto|自動|
|1〜3|弱〜強|

- louver
-- 風向きを指定する

|説明|値|
|:---:|:---:|
|Auto|自動|
|All|巡回|
|0〜4|前方〜真下|

- 使用例1
-- [三菱のルームエアコン(霧ヶ峰) MSZ-GV2216-W](https://www.mitsubishielectric.co.jp/ldg/wink/displayProduct.do?pid=262783&c040101410)に対して、下記の信号を送りたいときの例

|オプション名|説明|値|
|:---:|:---:|:---:|
|mode|モード|暖房|
|temperature|設定温度|23℃|
|wind|風量|2|
|louver|風向|1(真横が0〜真下が4)|

```
python ~/git/irmagician_data/mitsubishi_msz-gv2216.py --mode warm --temperature 22 --wind 2 --louver 1 | python ~/git/irmcli/irmcli.py -p -f -
```
