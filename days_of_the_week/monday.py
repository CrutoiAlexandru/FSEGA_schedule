import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

def monday(GROUP, LANG, SEMIG):
    tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

    if tm > clock.clock(9, 39) and tm < clock.clock(11, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["cuceu"])
            exit()
        if GROUP == '2':
            webbrowser.open(t.teachers["cuceu"])
            exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["cuceu"])
            exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["cuceu"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["cuceu"])
            exit()

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["silaghi"])
            exit()
        if GROUP == '2':
            webbrowser.open(t.teachers["silaghi"])
            exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["silaghi"])
            exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["silaghi"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["silaghi"])
            exit()

    elif tm > clock.clock(13, 59) and tm < clock.clock(15, 30):
        if GROUP == '1':
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
                exit()
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
                exit()
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
                exit()
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])
                exit()

        if GROUP == '2':
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
                exit()
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
                exit()
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
                exit()
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])
                exit()

        if GROUP == '3':
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
                exit()
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
                exit()
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
                exit()
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])
                exit()

        if GROUP == '4':
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
                exit()
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
                exit()
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
                exit()
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])
                exit()

        if GROUP == '5':
            if LANG == '1':
                webbrowser.open(t.teachers["ciupe"])
                exit()
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
                exit()
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
                exit()
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
                exit()
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])
                exit()

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["ciupe"])
            exit()
        if GROUP == '3':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
                exit()

    elif tm > clock.clock(17, 19) and tm < clock.clock(18, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["scridon"])
            exit()
        if GROUP == '2':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
                exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["ciupe"])
            exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["horvath"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["horvath"])
            exit()

    elif tm > clock.clock(18, 59) and tm < clock.clock(20, 30):
        if GROUP == '1':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
                exit()
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
                exit()
        if GROUP == '2':
            webbrowser.open(t.teachers["scridon"])
            exit()
        if GROUP == '3':
            webbrowser.open(t.teachers["horvath"])
            exit()
        if GROUP == '4':
            webbrowser.open(t.teachers["horvath"])
            exit()
        if GROUP == '5':
            webbrowser.open(t.teachers["horvath"])
            exit()

    else:
        main_window.noclass()     