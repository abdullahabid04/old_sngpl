from tkinter import *
from Projects.SUIGasProject.myutils import clear
from Projects.SUIGasProject.ProjectRequirements import COLORS, FONT_STYLE, FONT_SIZE, BOLD


class LoginScreen:
    def __init__(self, root, frame=None, user=None, imgs=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=COLORS["LIGHT_BLUE"])
        self.frame.pack(fill=BOTH, expand=True)

        txtlbl = ["<<<", "login", "email", "password", "email", "password", str(user) + '\t' + "LOGIN"]
        self.buttons = []
        self.entries = []
        for i in range(len(txtlbl)):
            if i <= 1:
                btn = Button(self.frame, text=txtlbl[i], bg=COLORS["BLUE"], fg=COLORS["LIGHT_BLUE"], width=7, height=2)
                btn.pack()
                btn.place(x=(510 * i) + 5, y=(495 * i) + 5)
                self.buttons.append(btn)
            elif 1 < i < 4:
                lbl = Label(self.frame, text=txtlbl[i], font=(FONT_STYLE, FONT_SIZE[15], BOLD), bg=COLORS["LIGHT_BLUE"],
                            fg=COLORS["BLUE"])
                lbl.pack()
                lbl.place(x=400, y=250 + (75 * (i - 1)))
            elif 3 < i < (len(txtlbl) - 1):
                entry = Entry(self.frame, width=20, font=(FONT_STYLE, FONT_SIZE[15]), bg=COLORS["BLUE"])
                entry.insert(0, txtlbl[i])
                entry.pack()
                entry.place(x=550, y=250 + (75 * (i - 3)))
                entry.bind("<Button-1>", lambda event, ent=entry: clear(event, ent))
                self.entries.append(entry)
            else:
                lbl = Label(self.frame, text=txtlbl[len(txtlbl) - 1], font=(FONT_STYLE, FONT_SIZE[15]),
                            bg=COLORS["LIGHT_BLUE"], fg=COLORS["BLUE"])
                lbl.pack()
                lbl.place(x=450, y=100)
        img = [imgs[1], imgs[2]]
        y = 325
        for i in range(len(img)):
            lb = Label(self.frame, image=img[i], bg=COLORS["BLUE"])
            lb.pack()
            lb.place(x=520, y=y)
            y = 400

    def destroy(self):
        self.frame.destroy()
