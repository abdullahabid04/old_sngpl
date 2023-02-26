from tkinter import *
from PIL import Image, ImageTk
from Projects.SUIGasProject.ProjectRequirements import *
from Projects.SUIGasProject.MainWindow import MainScreen
from Projects.SUIGasProject.WindowManager import open_login


root = Tk()

imgs = []
for i in range(len(images)):
    imgs.append(PhotoImage(file=images[i]))

icon = ImageTk.PhotoImage(Image.open("imgs/logo.png"))

root.title("S U I   N O R T H E R N   G A S   P A K   L I M I T E D")
root.iconphoto(root, icon)
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(width=False, height=False)
root.config(bg="Light Blue")

main_screen = MainScreen(root)
user_main = main_screen.option
btn_main = main_screen.btn
btn_main["command"] = lambda u=user_main: open_login(root, main_screen.frame, u, imgs, main_screen.destroy())

root.mainloop()
