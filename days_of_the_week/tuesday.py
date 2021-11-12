import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def tuesday(GROUP, LANG, SEMIG):
    if tm > clock.clock(9, 39) and tm < clock.clock(11, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["cuceu"])
            exit()

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["beleiu"])
            exit()
        if GROUP == '2':
            webbrowser.open(t.teachers["beleiu"])
            exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["beleiu"])
            exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["beleiu"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["beleiu"])
            exit()

    elif tm > clock.clock(13, 59) and tm < clock.clock(15, 30):
        if GROUP == '2':
            if LANG == '1':
                webbrowser.open(t.teachers["ciupe"])
                exit()

        if GROUP == '3':
            webbrowser.open(t.teachers["cirstea"])
            exit()

        if GROUP == '4':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
                exit()
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
                exit()

        if GROUP == '5':
            if main_window.week_type() == 0:
                webbrowser.open(t.teachers["dan"])
                exit()
            else:
                webbrowser.open(t.teachers["cuceu"])
                exit()

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if GROUP == '2':
            webbrowser.open(t.teachers["filip"])
            exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["scridon"])
            exit()
        if GROUP == '4':
            if LANG == '1':
                webbrowser.open(t.teachers["ciupe"])
                exit()
        if GROUP == '5':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
                exit()
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
                exit()

    elif tm > clock.clock(17, 19) and tm < clock.clock(18, 50):
        if GROUP == '3':
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
                exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["scridon"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["cirstea"])
            exit()

    elif tm > clock.clock(18, 59) and tm < clock.clock(20, 30):
        if GROUP == '4':
            webbrowser.open(t.teachers["cirstea"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["scridon"])
            exit()

    else:
        main_window.noclass()     