import os
import json
import pyperclip as pp
import TkEasyGUI as tk
import shutil

if shutil.which("xclip"):
    pp.set_clipboard("xclip")
elif shutil.which("xsel"):
    pp.set_clipboard("xsel")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = os.path.join(ROOT_DIR, 'clipbord-history.json')
MAX_HISTORY = 20

history = []
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

def save_history():
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def list_format(history):
    lf = lambda v: v.strip().replace("\n", "")
    short = lambda v: v[:20] + "..." if len(v) > 20 else v
    return [f"{i+1:02}: {lf(short(h))}" for i, h in enumerate(history)]

LAYOUT = [
    [tk.Text("履歴を選んで'コピーボタン'を押してください。")],
    [tk.Listbox(values=list_format(history), size=(40, 15), key="-history-")],
    [tk.Button("コピー"), tk.Button("削除"), tk.Button("終了")]
]

window = tk.Window("クリップボード履歴", LAYOUT)

while True:
    event, values = window.read(timeout=100)
    
    if event == "終了":
        tk.WINDOW_CLOSED
        break
    
    # コピーボタンの処理
    if event == "コピー":
        if values["-history-"]:
            set_text = values["-history-"][0]
            index = int(set_text[0:2])
            text = history[index - 1]
            pp.copy(text)
            tk.popup("コピーしました")
            
    # 削除ボタンの処理
    if event == "削除":
        if values["-history-"]:
            sel_text = values["-history-"][0]
            index = int(sel_text[0:2])
            
            # リストから該当要素を削除
            del history[index - 1]
            
            # 画面とファイルに更新内容を反映
            window["-history-"].update(list_format(history))
            save_history()
            
            # クリップボードを空にする処理は不要なため削除
            tk.popup("履歴を削除しました")
    
    # クリップボードの内容を監視
    new_text = pp.paste()

    # 空文字列、またはすでに存在する場合は処理をスキップ
    if not new_text or new_text in history:
        # 履歴が既に存在する場合は、順序を入れ替える
        if new_text and new_text in history:
            index = history.index(new_text)
            if index > 0:
                del history[index]
                history.insert(0, new_text)
                window["-history-"].update(list_format(history))
                save_history()
        continue # 処理を終えたらループの最初に戻る

    # 新しい履歴の追加
    history.insert(0, new_text)
    if len(history) > MAX_HISTORY:
        history.pop()

    # 画面とファイルに更新内容を反映
    window["-history-"].update(list_format(history))
    save_history()

window.close()
