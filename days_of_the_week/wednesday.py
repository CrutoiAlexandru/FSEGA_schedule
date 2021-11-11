import time
import webbrowser
import teachers as t
import clock

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def wednesday(GROUP, LANG, SEMIG):
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
            webbrowser.open(t.teachers["filip"])
        if GROUP == '2':
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
        if GROUP == '3':
            return 0
        if GROUP == '4':
            return 0
        if GROUP == '5':
            return 0

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["filip"])
        if GROUP == '2':
            webbrowser.open(t.teachers["filip"])
        if GROUP == '3':
            webbrowser.open(t.teachers["filip"])
        if GROUP == '4':
            webbrowser.open(t.teachers["filip"])
        if GROUP == '5':
            webbrowser.open(t.teachers["filip"])

    elif tm > clock.clock(13, 59) and tm < clock.clock(15, 30):
        if input("Doctrine = 1 or Fiscalitate = 2") == '1':
            webbrowser.open(t.teachers["rovinaru"])
        else:
            webbrowser.open(t.teachers["inceu"])

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if input("Management = 1 or Doctrine = 2") == '1':
            webbrowser.open(t.teachers["ilie"])
        else:
            webbrowser.open(t.teachers["manolachi"])

    elif tm > clock.clock(17, 19) and tm < clock.clock(18, 50):
        return 0

    elif tm > clock.clock(18, 59) and tm < clock.clock(20, 30):
        return 0

    else:
        time.sleep(30)
        monday(GROUP, LANG, SEMIG)
