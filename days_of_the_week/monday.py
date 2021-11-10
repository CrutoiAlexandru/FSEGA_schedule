import time
import webbrowser
import teachers as t
import clock

tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

def monday(GROUP, LANG, SEMIG):
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
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '3':
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '4':
            webbrowser.open(t.teachers["cuceu"])
        if GROUP == '5':
            webbrowser.open(t.teachers["cuceu"])

    elif tm > clock.clock(11, 19) and tm < clock.clock(12, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '2':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '3':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '4':
            webbrowser.open(t.teachers["silaghi"])
        if GROUP == '5':
            webbrowser.open(t.teachers["silaghi"])

    elif tm > clock.clock(13, 59) and tm < clock.clock(15, 30):
        if GROUP == '1':
            if LANG == '1':
                return 0
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])

        if GROUP == '2':
            if LANG == '1':
                return 0
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])

        if GROUP == '3':
            if LANG == '1':
                return 0
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])

        if GROUP == '4':
            if LANG == '1':
                return 0
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])

        if GROUP == '5':
            if LANG == '1':
                webbrowser.open(t.teachers["ciupe"])
            if LANG == '2':
                webbrowser.open(t.teachers["parasca"])
            if LANG == '3':
                webbrowser.open(t.teachers["feurdean"])
            if LANG == '4':
                webbrowser.open(t.teachers["sera"])
            if LANG == '5':
                webbrowser.open(t.teachers["tocalachis"])

    elif tm > clock.clock(15, 39) and tm < clock.clock(17, 10):
        if GROUP == '1':
            webbrowser.open(t.teachers["ciupe"])
        if GROUP == '2':
            return 0
        if GROUP == '3':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
        if GROUP == '4':
            return 0
        if GROUP == '5':
            return 0

    elif tm > clock.clock(17, 19) and tm < clock.clock(18, 50):
        if GROUP == '1':
            webbrowser.open(t.teachers["scridon"])
        if GROUP == '2':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
        if GROUP == '3':
            webbrowser.open(t.teachers["ciupe"])
        if GROUP == '4':
            webbrowser.open(t.teachers["horvath"])
        if GROUP == '5':
            webbrowser.open(t.teachers["horvath"])

    elif tm > clock.clock(18, 59) and tm < clock.clock(20, 30):
        if GROUP == '1':
            if SEMIG == '1':
                webbrowser.open(t.teachers["muresan"])
            if SEMIG == '2':
                webbrowser.open(t.teachers["pop"])
        if GROUP == '2':
            webbrowser.open(t.teachers["scridon"])
        if GROUP == '3':
            webbrowser.open(t.teachers["horvath"])
        if GROUP == '4':
            webbrowser.open(t.teachers["horvath"])
        if GROUP == '5':
            webbrowser.open(t.teachers["horvath"])

    else:
        time.sleep(30)
        monday(GROUP, LANG, SEMIG)