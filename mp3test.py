import pygame as pg
# 音声を再生するための準備
pg.mixer.init()
# 音声ファイルの読み込み
pg.mixer.music.load("Flip_Clock01-21(Far-Buzzer-50Hz).mp3")
# 音声を再生
pg.mixer.music.play()
print("再生開始")
# 再生が終了するまで待つ
while pg.mixer.music.get_busy():
  # 音声が流れている場合100ミリ秒待つ
  pg.time.wait(100)
print("再生終了")