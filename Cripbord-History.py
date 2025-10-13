import os #OSに関連する機能を使うモジュール
import json #Pythonオブジェクトとのデータとjsonファイルのデータを変換するモジュール
import pyperclip as pp
import TkEasyGUI as tk
import shutil
# pyperclipが使用するクリップボードツールを明示的に指定
if shutil.which("xclip"):
    pp.set_clipboard("xclip")
elif shutil.which("xsel"):
    pp.set_clipboard("xsel")

# クリップボードの履歴を保存するファイルパスと保存するファイル名を指定
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # 保存先となるファイルパスを指定
SAVE_FILE = os.path.join(ROOT_DIR,'clipbord-history.json') # 保存するファイル名の指定と保存先ファイルの作成
# 保存できる履歴の最大数を指定
MAX_HISTORY = 20

# 既存のクリップボード履歴を読み取る
history = [] # クリップボードの内容を保持するリスト
if os.path.exists(SAVE_FILE): # 保存先のファイルがある場合処理を行う
    with open(SAVE_FILE,"r",encoding="utf-8") as f: # 履歴の保存ファイルを開き文字コードの指定をして読み込む （rは読み込む(read)の意味)
        history = json.load(f)
# 履歴を保存する関数の作成
def save_history(): #関数の宣言
    with open(SAVE_FILE,"w",encoding="utf-8") as f: # 履歴保存ファイルを開く。今回は"w(write、書き込み)を指定し変更できるようにする
        json.dump(history,f,ensure_ascii=False,indent=2) #Pythonオブジェクト(historyリスト)をjsonに変換し履歴保存ファイルに保存
# 画面に表示する履歴の整形をする関数
def list_format(history): #関数の宣言と引数にhistoryリストを指定
# lambda関数（ラムダ関数、無名関数と呼ばれる簡単な処理を一時的に行うための関数）を使い各処理を定義
    lf = lambda v: v.strip().replace("\n","")  # strip関数で前後の空白文字(スペース、タブ,改行)を削除、replace関数で改行コード(\n)を空文字列("")に置換
    short = lambda v: v[:20] + "..." if len(v) > 20 else v  # 表示する履歴が20文字を超える場合、21字目以降の文字を"..."に置き換えて表示(保存した内容が変わるわけではない)
    return [f"{i+1:02}: {lf(short(h))}" for i, h in enumerate(history)] # 上記で定義したlambda関数を使い整形、履歴にインデックス(行番号)を付与した新しいリストを返す
# 表示するウィンドウのレイアウトを決める
LAYOUT = [
       [tk.Text("履歴を選んで'コピーボタン'を押してください。")], # 簡単な使い方説明を表示
       [tk.Listbox( # Listboxはリストの項目から選択を行えるようにする関数
                   # 選択肢の設定
                   values = list_format(history), #表示させる選択肢に 整形された履歴を指定
                   size = (40,15), # 画面に表示するウィンドウの大きさを指定
                   key="-history-" # 選択した履歴をリストから取得するためのキーを設定
           )],
       [# 各種ボタンの作成
        tk.Button("コピー"),tk.Button("削除"),tk.Button("終了")
        ]
       ]
# ウィンドウの作成
window = tk.Window("クリップボード履歴", LAYOUT)
# イベントループを使用しウィンドウ内の処理を実行
while True:
    # イベントを取得する
    event,values = window.read(timeout=100) # ウィンドウを読み込むイベントループの開始時間を100msに指定
    # 終了ボタンが押された場合処理を終了しウィンドウを閉じる
    if event == "終了":
        break
    # コピーボタンを押した場合の処理
    if event == "コピー":
        # 選択された履歴をクリップボードにコピー
        if values["-history-"]: # リストが空の状態かチェック
            set_text = values["-history-"][0] # LAYOUTで設定したキーを使い、リストの最初の文字列(index[0]、行番号)を取得
            index = int(set_text[0:2]) # 取得した文字列(行番号)から2文字目までを取り出す
            text = history[index - 1] # 行番号から1を引くことでリストに対応した正しいindexを算出、取得する値として指定(行番号01から1を引くと0になる)
            pp.copy(text) # 上記で指定したindexの値をクリップボードにコピー
            tk.popup("コピーしました")
    # 削除ボタンを押した場合
    if event == "削除":
        if values["-history-"]:
            sel_text = values["-history-"][0] # 行番号を取得
            # 履歴のデータを取り出す
            index = int(sel_text[0:2])
            del history[index - 1]
            window["-history-"].update(list_format(history)) # キーを使い取得した要素を更新前の状態で上書きする
            save_history() # 上記で上書きした内容を保存
            tk.popup("履歴を削除しました")
            pp.copy("") # 重複登録防止(削除してもクリップボードには値があるため、空文字列で上書きして履歴から完全に削除できるようにするため)
    # クリップボードの内容を確認し処理を行う
    text = pp.paste() # クリップボードの値を取得
    if text and text not in history:#クリップボードと履歴に値がない場合
        history.insert(0, text) # リストの先頭に追加
        if len(history) > MAX_HISTORY:
            history.pop()
        window["-history-"].update(list_format(history))
        save_history()
window.close()