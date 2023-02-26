from tkinter import *
from Projects.SUIGasProject.myutils import clear
from Projects.SUIGasProject.ProjectRequirements import COLORS, FONT_STYLE, FONT_SIZE


class SiteScreen:
    def __init__(self, root, frame=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=COLORS["LIGHT_BLUE"])
        self.frame.pack(fill=BOTH, expand=True)

        txt = ["name", "site", "time", "status", "alarm", "pressure"]
        self.entries = []
        for i in range(len(txt)):
            lbl = Label(self.frame, text=txt[i], bg=COLORS["LIGHT_BLUE"], fg=COLORS["BLUE"],
                        font=(FONT_STYLE, FONT_SIZE[13]))
            lbl.pack()
            lbl.place(x=225, y=300 + (50 * i))
            entry = Entry(self.frame)
            entry.pack()
            entry.place(x=300, y=300 + (50 * i))
            entry.insert(0, txt[i])
            entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
            self.entries.append(entry)

        for i in range(40):
            lbl = Label(self.frame, text="|", bg=COLORS["LIGHT_BLUE"], fg=COLORS["BLUE"])
            lbl.pack()
            lbl.place(x=570, y=20 * i)

        txt = ["<<<", "update", "plot"]
        y = [5, 720, 750]
        self.buttons = []

        for i in range(len(txt)):
            btn = Button(self.frame, text=txt[i], bg=COLORS["BLUE"], fg=COLORS["LIGHT_BLUE"], width=7, height=1)
            btn.pack()
            btn.place(x=5, y=y[i])
            self.buttons.append(btn)

    def destroy(self):
        self.frame.destroy()
