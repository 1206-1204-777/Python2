import pyperclip as pp
import TkEasyGUI as tk
import shutil
# pyperclipが使用するクリップボードツールを明示的に指定
if shutil.which("xclip"):
    pp.set_clipboard("xclip")
elif shutil.which("xsel"):
    pp.set_clipboard("xsel")
# 文字列をコピーする
pp.copy("test") # 実際に使う際はユーザーが入力した値が入る

# コピーした内容を取得
text = pp.paste()
# 取得した内容(test)をポップアップ表示
tk.popup(text)