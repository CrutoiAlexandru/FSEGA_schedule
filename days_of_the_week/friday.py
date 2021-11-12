import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def friday(GROUP, LANG, SEMIG):
    if tm > clock.clock(9, 39) and tm < clock.clock(11, 10):
        webbrowser.open(t.teachers["dragos"])
        exit()

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        webbrowser.open(t.teachers["popa"])
        exit()

    else:
        main_window.noclass()        