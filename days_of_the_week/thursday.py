import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def thursday(GROUP, LANG, SEMIG):
    if tm > clock.clock(7, 59) and tm < clock.clock(9, 30):
        webbrowser.open(t.teachers["mocean"])
        exit()

    elif tm > clock.clock(9, 39) and tm < clock.clock(11, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["mocean"])
            exit()
        if GROUP == '2':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["scortar"])
                exit()
            else:
                webbrowser.open(t.teachers["cuceu"])
                exit()
        if GROUP == '3':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["cuceu"])
                exit()
            else:
                webbrowser.open(t.teachers["scortar"])
                exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["mocean"])
            exit()

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["scortar"])
                exit()
            else:
                webbrowser.open(t.teachers["cuceu"])
                exit()
        if GROUP == '2':
            webbrowser.open(t.teachers["mocean"])
            exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["mocean"])
            exit()
        if GROUP == '4':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["cuceu"])
                exit()
            else:
                webbrowser.open(t.teachers["scortar"])
                exit()

    elif tm > clock.clock(13, 00) and tm < clock.clock(15, 30):
        main_window.bad_teacher()

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if GROUP == '5':
             webbrowser.open(t.teachers["mocean"])
             exit()

    else:
        main_window.noclass()     
