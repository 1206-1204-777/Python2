import os
import TkEasyGUI as sg


# 保存先やファイル名については変数などを使い動的に変更が可能
# 保存先のパスを指定
SCRIPT_DIR = os.path.dirname(__file__)
# 保存するファイル名と拡張子を指定。ただしPythonがこのファイルを操作する場合拡張子(.tex)は無視される
SAVE_FILE=os.path.join(SCRIPT_DIR , "notepad-save-test-data.tex")
# メモ帳の大きさなどレイアウトを指定
layout = [
    [sg.Multiline(size=(50,30),key="text")],# 行数と列数を指定し、書き込まれるデータをstr形式で保存
    [sg.Button("SAVE"),sg.Button("OPEN")],# 保存用とファイルを読み込む用のボタンを作成 
 ]
#表示するウィンドウを作成
window = sg.Window("memo", layout=layout)
# イベントループ
while True:
    #ウィンドウの内容を読み取る
    event,values = window.read()
    #閉じるボタンを押したときの挙動
    if event == sg.WINDOW_CLOSED:
        break
    # 保存ボタンを押した際の挙動
    if event == "SAVE":
        #ファイルに保存する処理。保存する場合は引数にw(write)を指定
        with open(SAVE_FILE,"w",encoding="utf-8") as f:
            f.write(values["text"])
            sg.popup("Saved")
    if event == "OPEN":
        #指定したファイルが存在するか確認
        if not os.path.exists(SAVE_FILE):
            sg.popup("Not Saved")
            continue
        # ファイルが存在する場合指定したファイルの読み込みを行う。読み込みの場合はr(read)を指定
        with open(SAVE_FILE,"r",encoding="utf-8") as f:
            text = f.read()
        # 読み込んだ内容をテキストボックスに反映(ウィンドウにファイルの内容を表示)
        window["text"].update(text)
window.close()