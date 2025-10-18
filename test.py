# 1.CSVデータをテキストとして読み込みカンマで区切る  - 不完全な方法
result = [] # 読み込んだデータを格納する配列reslutを作成
with open("test.csv","r",encoding= "utf-8") as fp: # 読み込むCSVファイル,読み込み専用として開く,文字エンコードの指定
    for line in fp.readlines():  #CSVファイルを 1行ずつ読み込む
        row = line.split(",") # 読み込んだファイル内容をカンマ区切る。ここが不完全な原因
        result.append(row) # 配列reslutにCSVから読み込んだデータを格納
# データが正しく読み込めたか確認
peach = result[2] # CSVファイルの3つ目のレコード"桃"の各データを取得できたか確認
print(f"(1) 果物: {peach[0] } 価格: {peach[2]}")  # 桃レコードの1番目(種類)と3番目(価格)のデータをfフォーマットを使い表示