from Projects.SUIGasProject.MainWindow import MainScreen
from Projects.SUIGasProject.LoginWindow import LoginScreen
from Projects.SUIGasProject.functionsbackend import login


def open_main(root, screen, imgs, function):
    main_screen = MainScreen(root, frame=screen)
    user = main_screen.option
    btn = main_screen.btn
    btn["command"] = lambda u=user: open_login(root, screen, u, imgs, main_screen.destroy())


def open_login(root, screen, user, imgs, function):
    login_screen = LoginScreen(root, frame=screen, user=user.get(), imgs=imgs)
    btn = login_screen.buttons
    entries = login_screen.entries
    cmds = [lambda r=root, s=login_screen.frame, im=imgs: open_main(r, s, im, login_screen.destroy()),
            lambda r=root, s=login_screen.frame, u=user, e=entries[0], p=entries[1]: login(r, s, u, e, p, imgs, open_main)]
    for i in range(len(cmds)):
        btn[i]["command"] = cmds[i]
