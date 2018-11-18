from tkinter import *

h = 1080
w = 1920
res = "1920x1080"


class Hello:
    def count(self):
        self.idx += 1
        self.lb.config(text="Hello world " + str(self.idx))
        return

    def __init__(self, window):
        self.window = window
        self.idx = 0
        window.title("Hello world")
        window.geometry(res)

        self.lb = Label(master=window, text="Hello world", font=("Arial", 20), fg="blue")
        self.lb.grid(row=10, column=520)

        self.bt = Button(master=window, text="Exit", font=("Helvetica", 15), command=sys.exit)
        self.bt.grid(row=100, column=500)

        self.bt2 = Button(master=window, text="Count", font=("Helvetica", 15), command=self.count)
        self.bt2.grid(row=100, column=800)


window = Tk()
hello = Hello(window)
window.mainloop()
