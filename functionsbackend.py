from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from random import randint
from Projects.SUIGasProject.getdatafromserver import read_data, write_data
from Projects.SUIGasProject.ProjectRequirements import *
from Projects.SUIGasProject.SiteWindow import SiteScreen


def login(root, screen, user, email, password, imgs, open_main):
    if user.get() == admin:
        if email.get() == email_admin and password.get() == password_admin:
            messagebox.showinfo("Administrator", "You are now logged in Administrator")
        else:
            messagebox.showwarning("Administrator", "Your password or email is incorrect")
    elif user.get() == calib:
        if email.get() == email_calibrator and password.get() == password_calibrator:
            messagebox.showinfo("Calibrator", "You are now logged in Calibrator")
        else:
            messagebox.showwarning("Calibrator", "Your password or email is incorrect")
    elif user.get() == oper:
        if email.get() == email_operator and password.get() == password_operator:
            site_screen = SiteScreen(root, frame=screen)
            btns = site_screen.buttons
            ent = site_screen.entries
            cmds = [lambda r=root, s=site_screen.frame: open_main(r, s, imgs, site_screen.destroy()),
                    lambda p=ent[5]: update(p), lambda win=site_screen.frame: plot_graph(win)]
            for i in range(len(btns)):
                btns[i]["command"] = cmds[i]
        else:
            messagebox.showwarning("Operator", "Your password or email is incorrect")
    else:
        messagebox.showerror("Invalid Option", "You entered an invalid option")


def update(p):
    try:
        press = p.get()
        write_data(press)
        p, t = read_data()
    except:
        t = str(randint(1, 12)) + " : " + str(randint(1, 59))
        p = randint(25, 50)

    graph_time.append(t)
    graph_pres.append(p)


def plot_graph(win):
    fig = Figure(figsize=(6, 8), dpi=90)
    fig.add_subplot(111).plot(graph_time[-5:len(graph_time)], graph_pres[-5:len(graph_pres)])
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().place(x=600, y=10)


def unused_function():
    print("Function called on button pressed")
