'''
デジタル時計の作成を開始
'''
import datetime
import TkEasyGUI as tk
 # 現在時刻を文字列として取得する関数を定義
def  get_time_now():
     now = datetime.datetime.now()
     return now.strftime("%H:%M:%S")
#表示する時計のレイアウトを指定
layout = [
    #表示する内容、フォントを指定
[tk.Text(get_time_now(),key="-output-",font=("Helvetica",80))],
# 時刻を更新するボタンを作成
[tk.Button("更新",font=("Helvetica",20))]
    ]
#ウィンドウの表示
window = tk.Window("テスト用デジタル時計", layout)
# ウィンドウ内の処理
while True:
    event = window.read()
    if event == tk.WINDOW_CLOSED:
        break
    if event == "更新":
        window["-output-"].update(get_time_now())
window.close()