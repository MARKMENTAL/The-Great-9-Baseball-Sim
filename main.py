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
    lbl1 = Label(window, text="", fg='red', font=("Cantarell", 12))
    if combobox1.get() != "":
        cputeamrnd = random.randint(0, 2)
        humanteamrnd = random.randint(0, 20)
        cputeam = combovalue[cputeamrnd]
        cputeamscore = random.randint(0,20)
        if humanteamrnd == cputeamscore:
            humanteamrnd += 1
        lbl1["text"] = "Feel Free to Keep Simming!"
        messagebox.showinfo(title="Game Results", message=(str(combobox1.get()),  humanteamrnd, cputeam, cputeamscore))
        lbl1.place(x=20, y=100)


def front(window1):
    btn = Button(window1, text="Sim Game", fg='green')
    btnabt = Button(window1, text="About", fg='navy')
    stringthing = btn['text']
    lbl = Label(window1, text="Player 1 Select a team to simulate as \n"
                " A random team will be the opponent ", fg='red', font=("Cantarell", 12))
    titlelbl = Label(window1, text="The Great 9 Baseball Sim: Milestone 0", fg='red', font=("Cantarell", 12))
    titlelbl.place(x=230, y=0)
    lbl.place(x=20, y=100)
    btn.place(x=70, y=50)
    btnabt.place(x=200, y=50)
    combobox = ttk.Combobox(state="readonly")
    combobox['value'] = ('Boston Boots', 'New York Americans', 'Seattle Sailors')
    combobox.place(x=50, y=150)
    btn.bind("<Button>", lambda e: back(lbl, combobox))
    btnabt.bind("<Button>", lambda e: about())
    btn.pack
    window1.mainloop()


def about():
    messagebox.showinfo(title="Author: MARKMENTAL666", message="Released under the GPLV3 \n Github.com/MARKMENTAL")


if __name__ == '__main__':
    window = Tk()
    window.title('The Great 9 Baseball Sim')
    window.geometry("720x480+10+20")
    front(window)
