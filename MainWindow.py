from tkinter import *
from Projects.SUIGasProject.ProjectRequirements import COLORS, FONT_STYLE


class MainScreen:
    def __init__(self, root, frame=None) -> None:
        if frame is not None:
            frame.destroy()
        self.frame = Frame(root, bg=COLORS["LIGHT_BLUE"])
        self.frame.pack(fill=BOTH, expand=True)

        x, y, txtlbl = [200, 300], [50, 250], ["S U I   N O R T H E R N   G A S   P A K   L I M I T E D",
                                               "S E L E C T   W H O   Y O U   A R E"]
        for i in range(len(txtlbl)):
            lbl = Label(self.frame, text=txtlbl[i], font=(FONT_STYLE, 25 - (5 * i)), bg=COLORS["LIGHT_BLUE"],
                        fg=COLORS["BLUE"])
            lbl.pack()
            lbl.place(x=x[i], y=y[i])

        options = ["Administrator", "Operator", "Calibrator"]
        self.option = StringVar()
        self.option.set(options[0])
        drop_menu = OptionMenu(self.frame, self.option, *options)
        drop_menu.pack()
        drop_menu.place(x=800, y=250)

        self.btn = Button(self.frame, text="SELECT", bg=COLORS["BLUE"], fg=COLORS["LIGHT_BLUE"], width=15, height=7,
                          justify=CENTER)
        self.btn.pack()
        self.btn.place(x=575, y=450)

    def destroy(self):
        self.frame.destroy()
