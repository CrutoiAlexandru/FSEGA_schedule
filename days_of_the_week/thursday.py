import time
import webbrowser
import teachers as t
import clock

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def thursday(GROUP, LANG, SEMIG):
    if tm > clock.clock(7, 59) and tm < clock.clock(9, 30):
        webbrowser.open(t.teachers["mocean"])

    elif tm > clock.clock(9, 39) and tm < clock.clock(11, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["mocean"])
        if GROUP == '2':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["scortar"])
            else:
                webbrowser.open(t.teachers["cuceu"])
        if GROUP == '3':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["cuceu"])
            else:
                webbrowser.open(t.teachers["scortar"])
        if GROUP == '4':
            webbrowser.open(t.teachers["mocean"])
        if GROUP == '5':
            return 0

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["scortar"])
            else:
                webbrowser.open(t.teachers["cuceu"])
        if GROUP == '2':
            webbrowser.open(t.teachers["mocean"])
        if GROUP == '3':
            webbrowser.open(t.teachers["mocean"])
        if GROUP == '4':
            if input("SI = 1 or SP = 2") == '1':
                webbrowser.open(t.teachers["cuceu"])
            else:
                webbrowser.open(t.teachers["scortar"])
        if GROUP == '5':
            return 0

    elif tm > clock.clock(13, 00) and tm < clock.clock(15, 30):
        print("Io nam optionalu si tanti nu da linku csf")

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if GROUP == '5':
             webbrowser.open(t.teachers["mocean"])
        else:
            return 0

    elif tm > clock.clock(17, 19) and tm < clock.clock(18, 50):
        return 0

    elif tm > clock.clock(18, 59) and tm < clock.clock(20, 30):
        return 0

    else:
        time.sleep(30)
        monday(GROUP, LANG, SEMIG)
