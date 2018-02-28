#!/usr/bin/env python3
from AddDLayout import AddDLayout
from SelectDLayout import SelectDLayout
from DatabaseManager import DatabaseManager
from tkinter.font import Font
import tkinter
import subprocess

class Checker(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.dManager = DatabaseManager()
        self.parent.title("Moje anime")
        self.parent.minsize(600, 1020)
        self.parent.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        label = tkinter.Label(self.parent, text="Čtenářský deník", font=Font(size=50))
        label.grid(row=0, column=0, columnspan=2)

        update_button = tkinter.Button(self.parent, text="Načíst změny", anchor="center", command=lambda: self.update_all())
        update_button.grid(row=1, column=0)

        update_button = tkinter.Button(self.parent, text="Otevřít soubory", anchor="center",
                                       command=lambda: self.open_files())
        update_button.grid(row=1, column=1)

        self.addDL = AddDLayout(self.parent, row=2)
        self.selectDL = SelectDLayout(self.parent, row=2,column=3)

    def update_all(self):
        self.addDL.create_layout()
        self.selectDL.create_layout()

    def open_files(self):
        subprocess.Popen(r'explorer /select, "C:\Users\balda\Desktop\MyProjects\AnimeChecker\DiaryDatabase\."')


root = tkinter.Tk()
app = Checker(root)
app.mainloop()