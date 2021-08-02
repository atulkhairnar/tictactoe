
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Tic Tac Toe")
        self.resizable(0, 0)
        # remove the minimize and maximize window option
        self.attributes('-toolwindow', True)

    def scoreboard(self):
        ttk.Button(self, text='New Game').grid(row=0, column=0)
        label = ttk.Label(self, text="Player 1: ").grid(row=0,column=0,columnspan=3,padx=10,pady=10)

    def gameboard(self):
        #frame = ttk.Frame(window)
        b0 = ttk.Button(self, text='O', style="C.TButton").grid(row=1, column=0)
        b1 = ttk.Button(self, text='X', style="C.TButton").grid(row=1, column=1)
        b2 = ttk.Button(self, text='O', style="C.TButton").grid(row=1, column=2)
        b3 = ttk.Button(self, text='O', style="C.TButton").grid(row=2, column=0)
        b4 = ttk.Button(self, text='X', style="C.TButton").grid(row=2, column=1)
        b5 = ttk.Button(self, text='X', style="C.TButton").grid(row=2, column=2)
        b6 = ttk.Button(self, text='O', style="C.TButton").grid(row=3, column=0)
        b7 = ttk.Button(self, text='X', style="C.TButton").grid(row=3, column=1)
        b8 = ttk.Button(self, text='O', style="C.TButton").grid(row=3, column=2)

        s = ttk.Style()
        s.configure('C.TButton', foreground='red', padding=30)

    def new_game(self):
        pass

    def play(self):
        self.scoreboard()
        self.gameboard()
        self.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = App()
    app.play()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
