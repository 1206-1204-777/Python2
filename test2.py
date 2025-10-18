import TkEasyGUI as sg 

# ファイル選択のダイアログを表示
file = sg.popup_get_file(
    "CSVファイルを選択してください。",
    multiple_files= False, # 単一のファイルの場合はFalseを指定
   # no_window=False,
    file_types=("CSVファイル","*.csv")
    )
sg.popup(file,"*.csv") # 指定したファイルパスを表示

# ファイル保存のダイアログ
file = sg.popup_get_file(
    "保存するCSVファイルを選択してください",
    save_as=True,
    file_types=(("CSVファイル",".*csv"),) 
    )
sg.popup(file,title="選択したファイル名")