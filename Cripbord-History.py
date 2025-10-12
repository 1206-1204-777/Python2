import pyperclip as pp
import TkEasyGUI as tk

# 文字列をコピーする
pp.copy("test") # 現在はハードコーディングだが、実際に使う際はユーザーが入力した値が入る

# コピーした内容を取得
test = pp.paste()
# 取得した内容(text)をポップアップ表示
tk.popup(test)