import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def wednesday(GROUP, LANG, SEMIG):
    if tm > clock.clock(9, 39) and tm < clock.clock(11, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["filip"])
            exit()
        if GROUP == '2':
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
                exit()

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["filip"])
            exit()
        if GROUP == '2':
            webbrowser.open(t.teachers["filip"])
            exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["filip"])
            exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["filip"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["filip"])
            exit()

    elif tm > clock.clock(13, 59) and tm < clock.clock(15, 30):
        if input("Doctrine = 1 or Fiscalitate = 2") == '1':
            webbrowser.open(t.teachers["rovinaru"])
            exit()
        else:
            webbrowser.open(t.teachers["inceu"])
            exit()

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if input("Management = 1 or Doctrine = 2") == '1':
            webbrowser.open(t.teachers["ilie"])
            exit()
        else:
            webbrowser.open(t.teachers["manolachi"])
            exit()

    else:
        main_window.noclass()     