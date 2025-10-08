import datetime as da
import pygame as pg
import TkEasyGUI as tk

# ツール全体の設定
SOUND_FILE = "Flip_Clock01-21(Far-Buzzer-50Hz).mp3" #使用する音声ファイルの指定し変数に代入
TIMER_SEC = 3 * 60 #タイマーの秒数を設定。今回は3分なので60(1分) x 3でこれを表す
# Mp3を再生するための事前準備
pg.mixer.init()
pg.mixer.music.load(SOUND_FILE) #指定された音声ファイルを読み込む
# タイマーのレイアウトを指定
Layout = [
    [tk.Label("00:00:00", key="-output-",font=("Helvetica",80))],
    [
     # スタートボタンの作成
     tk.Button("Start",font=("Helvetica",20)),
    # リセットボタンの作成
    tk.Button("Reset",font=("Helvetica",20))   
    ]
]
# ウィンドウの作成
window = tk.Window("3分タイマー",Layout)# ウィンドウのタイトルとレイアウトを指定
start_time = None #開始時間の初期化
# タイマー処理
while True:
    event,_ = window.read(timeout=10)
    if event == tk.WINDOW_CLOSED:
        break
    # スタートボタンを押した際の挙動
    if event == "Start":
        #開始時刻を記録
        start_time = da.datetime.now()
    #リセットボタンを押した際の挙動
    if event == "Reset":
        # タイマーを停止し初期状態に戻す
        start_time = None
        window["-output-"].update("00:00:00")
        # 音声再生中はそのまま継続
        if pg.mixer.music.get_busy():
            continue
    # タイマーが始まっていないときの処理
    if start_time is None:
        continue
    # 経過した時間の計算
    now = da.datetime.now() #現在時刻を取得
    delta = now - start_time # 現在時刻からタイマーの開始時間を引き差分を変数に格納
    #タイマー開始時間から現在時刻の差分が設定した時間(3分)に達した場合の処理
    if delta.seconds >= TIMER_SEC: 
        pg.mixer.music.play() # 音楽を再生
        start_time = None # タイマー開始時間をリセット
        window["-output-"].update("00:00:00") 
        continue
    # 残り時間を表示
    remain = TIMER_SEC - delta.seconds # 設定した時間(3分)からタイマー開始時間と現在時刻との差分を引く
    window["-output-"].update(
        "0" + str(da.timedelta(seconds=remain))) #冒頭に0をつけるのは時間表示をHH:MM:SSの形式に統一するため
window.close()