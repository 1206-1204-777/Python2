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
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # 保存するファイルパスを取得
SAVE_FILE = os.path.join(ROOT_DIR,'clipbord-history.json') # 保存するファイル名の指定
# 保存できる履歴の最大数を指定
MAX_HISTORY = 20

# 既存のクリップボード履歴を読み取る
history = [] # クリップボードの内容を保持する配列
if os.path.exists(SAVE_FILE): # もしも保存した履歴がある場合の処理
    with open(SAVE_FILE,"r",encoding="utf-8") as f: # 履歴の保存ファイルを開き文字コードの指定をして読み込む （rは読み込む(read)の意味)
        history = json.load(f)
# 履歴を保存する関数の作成
def save_history(): #関数の宣言
    with open(SAVE_FILE,"w",encoding="utf-8") as f: # 履歴保存ファイルを開く。今回は"w(write、書き込み)を指定し変更できるようにする
        json.dump(history,f,ensure_ascii=False,indent=2) #Pythonオブジェクト(history配列)をjsonに変換し 履歴保存ファイルに保存
#   履歴の整形をする関数
def list_format(history): #関数の宣言と引数にhistoryオブジェクトを指定
    lf = lambda v: v.strip().replace("\n","") 
    short = lambda v: v[:20] + "..." if len(v) > 20 else v
    return [f"{i+1:02}: {lf(short(h))}" for i, h in enumerate(history)]