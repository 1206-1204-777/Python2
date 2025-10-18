import csv 
import TkEasyGUI as sg

# ツールの基本動作を定義するmain関数を作成
def main():
    while True:
        file = sg.popup_get_file(
            "CSVファイルを選択してください",
            multiple_files=True, # 複数選択したいときはTrueを指定
            file_types=(("CSV","*.csv"),)
            )
        if len(file) ==0 or file == "": #選択したCSVファイルが存在しない場合は処理を中止
            break
        all_datas = []
        for filenames in file: #選択したファイルを変数に格納
            data = read_csv(filenames) #read_csv関数を使いcsvファイルを読み込む
            if data is None:
                sg.popup_error(filenames + "ファイルが読み込めません")
                continue
            # ヘッダーが重複する場合1つに統一
            if len(all_datas) >= 2 and len(data) >=2:
                if all_datas[0] == data[0]:
                    data = data[1:]
            all_datas += data
        if show_csv(all_datas) == False: # show_csv関数を使いテーブル表示する
            break
        
#read_csv関数を作成
def read_csv(filenames):
    try:
        with open(filenames,"r",encoding="utf-8") as f:
            reader =  csv.reader(f)
            data = [row for row in reader] #ファイルの内容を1行ずつ読み配列dataに格納
        return data
    except:
        pass
    return None #読み込みに市パイした場合は何も返さない

#CSVをテーブル表示するshow_csv関数を作成
def show_csv(data):
    if len(data) == 0: # 中身がない場合は空と表示する
        data = [["空"],["空"]]
    #表示するレイアウトを指定
    layout = [
        [sg.Table(
            key="-data-",
            values=data[1:],#データ(フィールド)を指定
            headings=data[0], # ヘッダー部分を指定
            expand_x=True,expand_y=True ,#テーブルの表示幅をウィンドウの大きさに合わせる
            justification="left" ,# 左詰めで表示
            auto_size_columns=True, #データに合わせてカラムの大きさを変える
            max_col_width=30, #カラムの最大値を指定
            font=("Aria",14))],
        [sg.Button("ファイルを選択"),sg.Button("保存"),sg.Button("終了")]
        ]
    # ウィンドウを作成
    window = sg.Window("CSV結合ツール",layout,size=(500,300),resizable=True)
    #イベントごとの処理
    flag = False
    while True:
        event,_ = window.read()
        if event in [sg.WINDOW_CLOSED,"終了"]:
            break
        #ファイル選択を選んだ場合フラグを変更
        if event == "ファイルを選択":
            flag = True
            break
        #ファイルの保存を選択した場合CSVファイルに書き込む
        if event == "保存":
            filenames = sg.popup_get_file(
                "保存するファイルを選択",
                save_as=True,
                file_types=(("CSV","*.csv"),)
                )
            if filenames == "" or filenames is None:
                continue
            with open(filenames,"w",encoding="utf-8",newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)
    window.close()
    return flag
if  __name__ == "__main__":
        main()