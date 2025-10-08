'''
デジタル時計の作成を開始
'''
import datetime
import TkEasyGUI as tk
#表示する時計のレイアウトを指定
layout = [
    #表示する内容、フォントを指定。時計に表示される初期値を00:00:00に設定
[tk.Label("00:00:00",key="-output-",font=("Helvetica",80))]
]
#時計を表示させるウィンドウの作成
window = tk.Window("テスト用デジタル時計", layout)
# ウィンドウ内の処理をイベントループで実行
while True:
    # イベントループの開始時間を10msに指定
    event, _ = window.read(timeout=10)
    if event == tk.WINDOW_CLOSED:
        break
    # 現在時刻を取得して表示
    now = datetime.datetime.now()
    window["-output-"].update(
        now.strftime("%H:%M:%S")
        )
window.close()