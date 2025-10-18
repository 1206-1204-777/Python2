# 1.CSVデータをテキストとして読み込みカンマで区切る  - 不完全な方法
result = [] # 読み込んだデータを格納する配列resultを作成
with open("test.csv","r",encoding= "utf-8") as fp: # CSVファイルをテキストとして読み込み
    for line in fp.readlines():  # ファイルの各行を順番に読み込み
        row = line.split(",") # カンマで区切り配列rowに格納
        result.append(row) # 配列resultにrowを追加
# データが正しく読み込めたか確認
peach = result[2] # CSVファイル3行目のデータを取得
print(f"(1) 果物: {peach[0] } 価格: {peach[2]}")  # index0:果物名とindex2:価格を表示
# 結果：(1) 果物: 桃 価格: "600"
# 2.CSVモジュールを使いCSVを読み込む
import csv # CSVモジュールをインポート
result = [] # 読み込んだデータを格納する配列resultを作成
with open("test.csv","r",encoding= "utf-8") as fp: # CSVファイルをテキストとして読み込み
    csv_reader = csv.reader(fp) # CSVモジュールの"reader"を使ったオブジェクトを作成
    for row in csv_reader:
        result.append(row)
# データが正しく読み込めたか確認
peach = result[2] # CSVファイル3行目のデータを取得
print(f"(1) 果物: {peach[0] } 価格: {peach[2]}")  # index0:果物名とindex2:価格を表示
#結果：(1) 果物: 桃 価格: 600