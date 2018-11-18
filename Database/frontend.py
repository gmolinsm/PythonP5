from tkinter import *
import Database.backend


class Frontend(object):

    def __init__(self, window):
        self.window = window
        self.backend = Database.backend.Backend()
        window.title("Database")
        myfont = ("Times New Roman", 18)

        # start with the labels
        self.lbl1 = Label(master=window, text="Title", font=myfont)
        self.lbl1.grid(row=0, column=0)

        self.lbl2 = Label(master=window, text="Year", font=myfont)
        self.lbl2.grid(row=0, column=2)

        self.lbl3 = Label(master=window, text="Director", font=myfont)
        self.lbl3.grid(row=1, column=0)

        self.lbl4 = Label(master=window, text="Actress/Actor", font=myfont)
        self.lbl4.grid(row=1, column=2)

        # create the entries
        self.name_text = StringVar()
        self.et1 = Entry(master=window, textvariable=self.name_text, font=myfont)
        self.et1.grid(row=0, column=1)

        self.date_text = StringVar()
        self.et2 = Entry(master=window, textvariable=self.date_text, font=myfont)
        self.et2.grid(row=0, column=3)

        self.director_text = StringVar()
        self.et3 = Entry(master=window, textvariable=self.director_text, font=myfont)
        self.et3.grid(row=1, column=1)

        self.lead_text = StringVar()
        self.et4 = Entry(master=window, textvariable=self.lead_text, font=myfont)
        self.et4.grid(row=1, column=3)

        # Create the ListBox
        self.listbox = Listbox(master=window, height=10, width=40, font=("Times New Roman", 15))
        self.listbox.grid(row=2, column=0, rowspan=8, columnspan=2)

        self.scroll = Scrollbar(master=window)
        self.scroll.grid(row=2, column=2, rowspan=8, sticky="nsw")

        self.listbox.bind('<<ListboxSelect>>', self.get_row)

        # Link the scrollbar to the listbox
        self.scroll.configure(command=self.listbox.yview)

        # Buttons
        self.bt1 = Button(master=window, text="View all", width=10, font=myfont, command=self.view_command)
        self.bt1.grid(row=3, column=3)

        self.bt2 = Button(master=window, text="Add", width=10, font=myfont, command=self.add_command)
        self.bt2.grid(row=4, column=3)

        self.bt3 = Button(master=window, text="Delete", width=10, font=myfont, command=self.delete_command)
        self.bt3.grid(row=5, column=3)

        self.bt4 = Button(master=window, text="Search", width=10, font=myfont)
        self.bt4.grid(row=6, column=3)

        self.bt5 = Button(master=window, text="Close", width=10, font=myfont, command=self.close)
        self.bt5.grid(row=7, column=3)

    def view_command(self):
        self.listbox.delete(0, END)
        rows = self.backend.view_all()
        for line in rows:
            self.listbox.insert(END, line)

    def add_command(self):
        self.listbox.delete(0, END)
        title = self.lead_text.get()
        director = self.director_text.get()
        year = self.date_text.get()
        lead = self.lead_text.get()
        self.backend.add(title=title, director=director, year=year, lead=lead)
        self.listbox.insert(END, (title, director, year, lead))

    def get_row(self, event=None):
        index = self.listbox.curselection()[0]
        line = self.listbox.get(index)
        self.name_text.set(line[1])
        self.director_text.set(line[2])
        self.date_text.set(line[3])
        self.lead_text.set(line[4])
        return line

    def delete_command(self):
        line = self.get_row()
        self.backend.delete(line[0])
        self.view_command()

    def close(self):
        exit(0)


window = Tk()
front = Frontend(window)
window.mainloop()