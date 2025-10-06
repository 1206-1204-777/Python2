import TkEasyGUI as sg
layout = [
    [sg.Text("足掻け"),sg.Text("勝つまで")],
    [sg.Button("OK")]
    ]
window = sg.Window("testComment",layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "OK":
        sg.popup("ボタン押されました")
        break
window.close()