from pathlib import Path
import tkinter
from tkinter import filedialog
import openpyxl


class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280, border=1, relief="groove")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        # 閉じるボタンを実装
        quit_btn = tkinter.Button(self)
        quit_btn["text"] = "閉じる"
        quit_btn["command"] = self.root.destroy
        quit_btn.pack(side="bottom")

        # textboxを作る
        # 入力されたテキストを何か処理をしたいから
        # self.でインスタンス変数として保存
        self.text_box = tkinter.Entry(self)
        self.text_box["width"] = 30
        self.text_box.pack()

        # 実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn["text"] = "実行"
        # submit_btn["command"] = self.input_handler
        submit_btn["command"] = self.save_data
        submit_btn.pack()

        # メッセージ出力
        self.message = tkinter.Message(self)
        self.message.pack()

    def input_handler(self):
        text = self.text_box.get()
        self.message["text"] = text + "!!"

    def save_data(self):
        text = self.text_box.get()
        file_name = filedialog.askopenfilename(initialdir=Path.cwd())
        wb = openpyxl.load_workbook(file_name)
        ws = wb.worksheets[0]
        ws["B1"].value = text
        wb.save(file_name)
        self.message["text"] = "保存完了"
