import time
import webbrowser
import teachers as t
import clock

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def tuesday(GROUP, LANG, SEMIG):
    if tm > clock.clock(7, 59) and tm < clock.clock(9, 30):
        if GROUP == '1':
            return 0
        if GROUP == '2':
            return 0
        if GROUP == '3':
            return 0
        if GROUP == '4':
            return 0
        if GROUP == '5':
            return 0

    elif tm > clock.clock(9, 39) and tm < clock.clock(11, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '2':
            return 0
        if GROUP == '3':
            return 0
        if GROUP == '4':
            return 0
        if GROUP == '5':
            return 0

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["beleiu"])
        if GROUP == '2':
            webbrowser.open(t.teachers["beleiu"])
        if GROUP == '3':
            webbrowser.open(t.teachers["beleiu"])
        if GROUP == '4':
            webbrowser.open(t.teachers["beleiu"])
        if GROUP == '5':
            webbrowser.open(t.teachers["beleiu"])

    elif tm > clock.clock(13, 59) and tm < clock.clock(15, 30):
        if GROUP == '1':
            return 0

        if GROUP == '2':
            if LANG == '1':
                webbrowser.open(t.teachers["ciupe"])

        if GROUP == '3':
            webbrowser.open(t.teachers["cirstea"])

        if GROUP == '4':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])

        if GROUP == '5':
            week = input("SI = 1 or SP = 2")
            if week == 1:
                webbrowser.open(t.teachers["dan"])
            else:
                webbrowser.open(t.teachers["cuceu"])

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if GROUP == '1':
            return 0
        if GROUP == '2':
            webbrowser.open(t.teachers["filip"])
        if GROUP == '3':
            webbrowser.open(t.teachers["scridon"])
        if GROUP == '4':
            if LANG == '1':
                webbrowser.open(t.teachers["ciupe"])
        if GROUP == '5':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])

    elif tm > clock.clock(17, 19) and tm < clock.clock(18, 50):
        if GROUP == '1':
            return 0
        if GROUP == '2':
            return 0
        if GROUP == '3':
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
        if GROUP == '4':
            webbrowser.open(t.teachers["scridon"])
        if GROUP == '5':
            webbrowser.open(t.teachers["cirstea"])

    elif tm > clock.clock(18, 59) and tm < clock.clock(20, 30):
        if GROUP == '1':
            return 0
        if GROUP == '2':
            return 0
        if GROUP == '3':
            return 0
        if GROUP == '4':
            webbrowser.open(t.teachers["cirstea"])
        if GROUP == '5':
            webbrowser.open(t.teachers["scridon"])

    else:
        time.sleep(30)
        monday(GROUP, LANG, SEMIG)