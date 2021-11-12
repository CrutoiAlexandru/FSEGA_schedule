import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def wednesday(GROUP, LANG, SEMIG, OPTIONAL):
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
        if OPTIONAL == '1':
            webbrowser.open(t.teachers["rovinaru"])
            exit()
        if OPTIONAL == '3':
            webbrowser.open(t.teachers["inceu"])
            exit()

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if OPTIONAL == '2':
            webbrowser.open(t.teachers["ilie"])
            exit()
        if OPTIONAL == '1':
            webbrowser.open(t.teachers["manolachi"])
            exit()

    else:
        main_window.noclass()     