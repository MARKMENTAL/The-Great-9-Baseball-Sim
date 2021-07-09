from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox


def back(lbl1, combobox1):
    lbl1.destroy()
    cputeamrnd = 0
    humanteamrnd = 0
    cputeam = ""
    humanteam = ""
    combovalue = combobox1["value"]
    lbl1 = Label(window, text="", fg='green', font=("Cantarell", 12))
    if combobox1.get() != "":
        cputeamrnd = random.randint(0, 9)
        humanteamrnd = random.randint(0, 20)
        cputeam = combovalue[cputeamrnd]
        cputeamscore = random.randint(0, 20)
        btnabt = Button(window, text="About", fg='navy')
        btnabt.place(x=200, y=50)
        btnabt.bind("<Button>", lambda e: about())
        if humanteamrnd == cputeamscore:
            humanteamrnd = humanteamrnd + 1
        lbl1["text"] = "Feel Free to Keep Simming!"
        messagebox.showinfo(title="Game Results", message=(str(combobox1.get()),  humanteamrnd, cputeam, cputeamscore))
        if humanteamrnd > cputeamscore:
            messagebox.showinfo(title="Game Results", message=("The ", str(combobox1.get()), " won! \n Good Job"))
        lbl1.place(x=20, y=100)
    if combobox1.get() == "":
        lbl1["text"] = "Please Select a Team"
        lbl1.place(x=20, y=100)


def front(window1):
    menubar = Menu(window1)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=window1.quit)
    filemenu.add_command(label="About", command=about)
    menubar.add_cascade(label="Options", menu=filemenu)
    window1.config(menu=menubar)
    btn = Button(window1, text="Sim Game", fg='green')
    lbl = Label(window1, text="Player 1 Select a team to simulate as \n"
                " A random team will be the opponent ", fg='red', font=("Cantarell", 12))
    titlelbl = Label(window1, text="The Great 9 Baseball Sim: Milestone 1", fg='red', font=("Cantarell", 12))
    titlelbl.place(x=230, y=0)
    lbl.place(x=20, y=100)
    btn.place(x=70, y=50)
    combobox = ttk.Combobox(state="readonly")
    combobox['value'] = ('Boston Boots', 'New York Americans', 'Seattle Sailors'
                         , "San Francisco Titans", "California Seraphims", "Buffalo Blue Birds", "Tokyo Tornadoes"
                         , "Wyoming Westerners", "London Lookout", "Virginia Turkeys")
    combobox.place(x=50, y=150)
    btn.bind("<Button>", lambda e: back(lbl, combobox))

    btn.pack
    window1.mainloop()


def about():
    messagebox.showinfo(title="Author: MARKMENTAL666", message="Released under the GPLV3 \n Github.com/MARKMENTAL")


if __name__ == '__main__':
    window = Tk()
    window.title('The Great 9 Baseball Sim')
    window.geometry("720x480+10+20")
    front(window)
